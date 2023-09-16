import abc
import json
from typing import List, Dict

import duckdb

from core.tool import extract_variable


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
        # 下一步
        self.next_nodes: List[IPlugin] = []
        # 上一步
        self.pre_nodes: List[IPlugin] = []
        # 设置结果
        self._pre_result_dict: Dict[str, duckdb.DuckDBPyRelation] = {}
        # 当前任务Flow
        from core.flow import Flow
        self.flow: Flow = None

    def execute(self):
        pass

    def init(self, param: json, flow):
        self.id = param["id"]
        self.type = param["type"]
        self.name = param["name"]
        self.param = param["properties"]
        self.flow = flow

    def set_result(self, df: duckdb.DuckDBPyRelation):
        self.flow.con.commit()
        # 设置结果
        for node in self.next_nodes:
            node._pre_result_dict[self.name] = df
        # 执行下一步
        for node in self.next_nodes:
            node.before_execute()
            node.execute()
            node.after_execute()

    # 关闭资源
    def close(self):
        if self.status != "STOP":
            self.status= "STOP"
            # 执行下一步
            for node in self.next_nodes:
                node.close()

    def before_execute(self):
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
        # 变量还原
        for key, value in self.shadow_variable_param.items():
            self.param[key] = value

    def to_json(self):
        return {
            "name": self.name,
            "id": self.id,
            "type": self.type,
            "properties": self.param
        }
