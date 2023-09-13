import abc
import uuid
from enum import Enum

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
        print("创建Flow", self.flow_uid)

    def add_node(self, node: IPlugin):
        return self

    def set_edge(self, start_id: str, end_id: str):
        return self

    # 设置flow层级的参数
    def set_param(self, param_dict: dict):
        return self

    # 提交任务
    def run(self):
        pass

    # flow转json
    def to_flow_str(self):
        pass
