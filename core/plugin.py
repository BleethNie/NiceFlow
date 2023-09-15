import abc
import json
from typing import List, Dict

from pandas import DataFrame

from core.flow import Flow


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
        self._pre_result_dict: Dict[str, DataFrame] = {}
        # 当前任务Flow
        self.flow: Flow = None

    # 带参数的装饰器
    def query(self):
        def wrapper(func):
            def sub_wrapper(*args, **kwargs):
                # 打印装饰器的参数
                print(f'查询方式：{self.name}')
                # 返回函数运行结果
                return func(*args, **kwargs)

            return sub_wrapper

        return wrapper

    def execute(self):
        pass

    def init(self, param: json, flow: Flow):
        self.id = param["id"]
        self.type = param["type"]
        self.name = param["name"]
        self.param = param["properties"]
        self.flow = flow

    def set_result(self, df: DataFrame):
        # 设置结果
        for node in self.next_nodes:
            node._pre_result_dict[self.name] = df
        # 执行下一步
        for node in self.next_nodes:
            node.execute()

    # 关闭资源
    def close(self):

        pass

    def to_json(self):
        return {
            "name": self.name,
            "id": self.id,
            "type": self.type,
            "properties": self.param
        }
