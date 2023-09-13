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
        # class名称
        self.next_nodes = []

    def init(self, param: json):
        self.id = param["id"]
        self.type = param["type"]
        self.name = param["name"]
        print(param)

    @abc.abstractmethod
    def execute(self):
        pass
