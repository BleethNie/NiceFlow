import abc
import json
from typing import List, Dict

import duckdb
from event_bus import EventBus
from loguru import  logger
from src.core.tool import extract_variable


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
        from src.core.plugin_time_record import PluginTimeRecord
        self.run_record: PluginTimeRecord = PluginTimeRecord(self)
        # 当前任务Flow
        from src.core.flow import Flow
        self.flow: Flow = None

    def execute(self):
        pass

    def init(self, param: json, flow):
        self.id = param["id"]
        self.type = param["type"]
        self.name = param["name"]
        self.param = param["properties"]
        self.flow = flow
        self.bus: EventBus = self.flow.bus
        event = f"{self.id}:{self.name}"
        event_after = f"{self.id}:{self.name}:after"
        self.bus.add_event(self.execute, event)
        self.bus.add_event(self.after_execute, event_after)

    def set_result(self, df: duckdb.DuckDBPyRelation):
        # 设置结果
        self.df_count = len(df)
        for node in self.next_nodes:
            node._pre_result_dict[self.name] = df
        # 执行下一步
        for node in self.next_nodes:
            node.before_execute()
            if len(node._pre_result_dict) < len(node.pre_nodes):
                continue
            node.bus.emit(event=f"{node.id}:{node.name}")
            logger.debug("event 执行完后执行after")
            node.bus.emit(event=f"{node.id}:{node.name}:after")

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
        for key, value in self.param.items():
            # 判断是变量，则进行更新
            if "${" not in str(value):
                continue
            for flow_key, flow_value in self.flow.param_dict.items():
                var_flow_key = "${" + flow_key + "}"
                if var_flow_key in str(value):
                    self.param[key] = str(value).replace(var_flow_key, str(flow_value))
                    # 设置影子变量
                    if key not in self.shadow_variable_param:
                        self.shadow_variable_param[key] = value

    def after_execute(self):
        logger.debug("执行after。。。")
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
