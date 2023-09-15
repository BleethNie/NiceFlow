import abc
import uuid
from enum import Enum
from typing import List

import duckdb

from core.plugin import IPlugin


class FlowStatusEnum(Enum):
    WAITING = 0,
    RUNNING = 1,
    FAIL = 2,
    SUCCESS = 3,


class Flow(metaclass=abc.ABCMeta):

    def __init__(self):
        self.flow_uid = uuid.uuid1()
        self.flow_status: FlowStatusEnum = FlowStatusEnum.WAITING
        self.plugin_dict: dict[str, IPlugin] = {}
        self.con = duckdb.connect()
        self.param_dict: dict[str, object] = {}
        print("创建Flow", self.flow_uid)

    def add_node(self, node: IPlugin):
        self.plugin_dict[node.name] = node
        return self

    def set_edge(self, start_id: str, end_id: str):
        start_node = self.plugin_dict[start_id]
        end_node = self.plugin_dict[end_id]
        start_node.next_nodes.append(end_node)
        end_node.pre_nodes.append(start_node)
        return self

    def get_flow_uid(self):
        return self.flow_uid

    # 设置flow层级的参数
    def set_param(self, param_dict: dict):
        self.param_dict.update(param_dict)
        return self

    # 提交任务
    def run(self):
        # 找到首节点
        for key in self.plugin_dict.keys():
            node: IPlugin = self.plugin_dict[key]
            pre_nodes: List[IPlugin] = node.pre_nodes
            if len(pre_nodes) == 0:
                # 找到首节点
                node.before_execute()
                node.execute()

        # 按照顺序关闭资源
        for key in self.plugin_dict.keys():
            node: IPlugin = self.plugin_dict[key]
            pre_nodes: List[IPlugin] = node.pre_nodes
            if len(pre_nodes) == 0:
                # 找到首节点
                node.close()

    # 关闭资源
    def close(self):
        self.con.close()

    # flow转json
    def to_flow_json(self):
        nodes = []
        edges = []
        for key in self.plugin_dict.keys():
            node: IPlugin = self.plugin_dict[key]
            nodes.append(node.to_json())
            pre_nodes: List[IPlugin] = node.pre_nodes
            for node in pre_nodes:
                edges.append({"startId": node.name, "endId": node.name})
        return {"nodes": nodes, "edges": edges}
