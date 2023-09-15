import abc
import json
from typing import List, Dict

import duckdb


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

    # 关闭资源
    def close(self):
        # 执行下一步
        for node in self.next_nodes:
            node.close()

    def before_execute(self):
        # 变量更新
        for key, value in self.param.items():
            # 判断是变量，则进行更新
            if str(value).startswith("${") and str(value).endswith("}"):
                variable = str(value).removeprefix("${").removesuffix("}")
                self.param[key] = self.flow.param_dict[variable]

    def to_json(self):
        return {
            "name": self.name,
            "id": self.id,
            "type": self.type,
            "properties": self.param
        }
