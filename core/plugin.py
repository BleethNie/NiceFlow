import abc
import json


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
        self.next_nodes = []
        # 上一步
        self.pre_nodes = []

    def init(self, param: json):
        self.id = param["id"]
        self.type = param["type"]
        self.name = param["name"]
        self.param = param["properties"]

    @abc.abstractmethod
    def execute(self):
        pass


    def to_json(self):
        pass