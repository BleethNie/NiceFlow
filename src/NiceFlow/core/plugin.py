import abc
import json
from typing import List, Dict

import duckdb
import loguru
from blinker import signal

from NiceFlow.core.tool import extract_variable, replace_vars


class IPlugin(metaclass=abc.ABCMeta):

    def __init__(self):
        # 同一个flow中唯一
        self.name = ""
        # input,output,agg等
        self.type = ""
        # class名称
        self.id = ""
        # 参数
        self.param = {}
        # 设置plugin状态
        self.status = ""
        # 影子参数
        self.shadow_variable_param = {}
        # 字段注释信息
        self.plugin_fields = []
        # 下一步
        self.next_nodes: List[IPlugin] = []
        # 上一步
        self.pre_nodes: List[IPlugin] = []
        # 处理数据量
        self.df_count: int = 0
        # 设置结果
        self._pre_result_dict: Dict[str, duckdb.DuckDBPyRelation] = {}
        # 记录任务执行时间和次数
        from NiceFlow.core.plugin_time_record import PluginTimeRecord
        self.run_record: PluginTimeRecord = PluginTimeRecord(self)
        # 当前任务Flow
        from NiceFlow.core.flow import Flow
        self.flow: Flow = None
        # 设置信号
        self.signal = signal(self.name + "execute")

    def receiver(self, sender):
        if len(self.pre_nodes) > len(self._pre_result_dict):
            return
        self.execute()

    def execute(self):
        self.before_execute()

    def init(self, param: json, flow):
        self.id = param["id"]
        self.type = param["type"]
        self.name = param["name"]
        self.param = param["properties"]
        self.flow = flow

        # self.bus: EventBus = self.flow.bus
        # event = f"{self.id}:{self.name}"
        # event_after = f"{self.id}:{self.name}:after"
        # self.bus.add_event(self.execute, event)
        # self.bus.add_event(self.after_execute, event_after)

    def set_result(self, df: duckdb.DuckDBPyRelation = None):
        # 设置结果
        self.df_count = 0 if df is None else len(df)
        # 如果是最后一个节点则将结果信息给到flow
        if len(self.next_nodes) == 0:
            self.flow.set_result(self.name, df)

        for node in self.next_nodes:
            node._pre_result_dict[self.name] = df
        # 执行下一步
        for node in self.next_nodes:
            self.signal.connect(node.receiver, sender=self)
            # if len(node._pre_result_dict) < len(node.pre_nodes):
            #     continue
            # node.bus.emit(event=f"{node.id}:{node.name}")
            # logger.debug("event 执行完后执行after")
            # node.bus.emit(event=f"{node.id}:{node.name}:after")
        self.after_execute()
        self.signal.send(self)

    # 关闭资源
    def close(self):
        if self.status != "STOP":
            self.status = "STOP"
            # 执行下一步
            for node in self.next_nodes:
                node.close()

    def before_execute(self):
        # 记录执行开始时间
        self.run_record.start()
        if len(self.shadow_variable_param) > 0:
            for key, value in self.shadow_variable_param.items():
                variable_list = extract_variable(str(value))
                for variable in variable_list:
                    flow_value = self.flow.param_dict[variable]
                    var_key = "${" + variable + "}"
                    self.param[key] = str(value).replace(var_key, str(flow_value))
        # 变量更新
        for param_key, param_value in self.param.items():
            new_param_value, is_contains_var = replace_vars(param_value, self.flow.param_dict)
            if is_contains_var:
                self.param[param_key] = new_param_value
                if param_key not in self.shadow_variable_param:
                    self.shadow_variable_param[param_key] = param_value

    def after_execute(self):
        loguru.logger.debug("【{}】执行after", self.name)
        # 记录执行结束时间
        self.run_record.stop()
        self.run_record.print()
        # 变量还原
        for key, value in self.shadow_variable_param.items():
            self.param[key] = value

    def __param_check(self):
        # 必要参数校验失败则直接退出
        pass

    def to_json(self):
        return {
            "name": self.name,
            "id": self.id,
            "type": self.type,
            "properties": self.param
        }
