import abc
import logging
import uuid
from enum import Enum
from typing import List

import duckdb
# from event_bus import EventBus
from blinker import signal
from loguru import logger

from NiceFlow.core.plugin import IPlugin


class FlowStatusEnum(Enum):
    WAITING = 0,
    RUNNING = 1,
    FAIL = 2,
    SUCCESS = 3,


class Flow(metaclass=abc.ABCMeta):

    def __init__(self, work_dir: str = None):
        self.flow_uid = uuid.uuid1()
        self.flow_status: FlowStatusEnum = FlowStatusEnum.WAITING
        self.plugin_dict: dict[str, IPlugin] = {}
        if work_dir == None:
            self.con = duckdb.connect()
        self.param_dict: dict[str, object] = {}
        self.start_signal = signal("")
        logger.info("Flow Task创建成功,FlowUid = 【{}】".format(self.flow_uid))

    @classmethod
    def register_log_handler(cls, handler: logging.Handler = None):
        if handler is None:
            logger.configure(handlers=[{"sink": logging.StreamHandler, "serialize": True}])
        else:
            logger.configure(handlers=[{"sink": handler, "serialize": True}])

    def add_node(self, node: IPlugin):
        self.plugin_dict[node.name] = node
        return self

    def add_triple(self, start_node: IPlugin,end_node: IPlugin):
        self.plugin_dict[start_node.name] = start_node
        self.plugin_dict[end_node.name] = end_node
        self.set_edge(start_node.name,end_node.name)
        return self

    def set_edge(self, start_id: str, end_id: str):
        start_node = self.plugin_dict[start_id]
        end_node = self.plugin_dict[end_id]
        start_node.next_nodes.append(end_node)
        end_node.pre_nodes.append(start_node)
        return self

    def set_project_root_path(self, root_path: str):
        self.param_dict["root_path"] = root_path
        return self

    def get_flow_uid(self):
        return self.flow_uid

    # 设置flow层级的参数
    def set_param(self, param_dict: dict):
        self.param_dict.update(param_dict)
        return self

    # 提交任务
    def run(self, df: duckdb.DuckDBPyRelation = None):
        # 找到首节点
        for key in self.plugin_dict.keys():
            node: IPlugin = self.plugin_dict[key]
            pre_nodes: List[IPlugin] = node.pre_nodes
            if len(pre_nodes) == 0:
                self.start_signal.connect(node.receiver, sender=self)
        self.start_signal.send(self)

        # 按照顺序关闭资源
        for key in self.plugin_dict.keys():
            node: IPlugin = self.plugin_dict[key]
            pre_nodes: List[IPlugin] = node.pre_nodes
            if len(pre_nodes) == 0:
                # 找到首节点
                node.close()

    # stream方式处理数据
    def stream(self, df: duckdb.DuckDBPyRelation = None):
        # 找到首节点
        for key in self.plugin_dict.keys():
            node: IPlugin = self.plugin_dict[key]
            pre_nodes: List[IPlugin] = node.pre_nodes
            if len(pre_nodes) == 0:
                # 找到首节点
                node.before_execute()
                node.execute()
                node.after_execute()

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
