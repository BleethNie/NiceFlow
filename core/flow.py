import abc
from enum import Enum


class FlowStatusEnum(Enum):
    RUNNING = 1,
    FAIL = 2,
    SUCCESS = 3,
    PREVIEW = 4,


class Flow(metaclass=abc.ABCMeta):

    def __init__(self):
        self.flowUid = ""
        self.flowStatus = ""

    # 从json加载flow
    @classmethod
    def load(cls, content: str):
        Flow()

    # 提交任务
    def submit(self):
        pass

    # flow转json
    def to_flow_str(self):
        pass
