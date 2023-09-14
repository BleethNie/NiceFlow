import abc
import json
import time
from functools import wraps
from typing import List, Dict
from pandas import DataFrame



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


    @abc.abstractmethod
    def execute(self):
        pass

    def init(self, param: json):
        self.id = param["id"]
        self.type = param["type"]
        self.name = param["name"]
        self.param = param["properties"]

    def set_result(self, node_id: str, df: DataFrame):
        self._pre_result_dict[node_id] = df

    def to_json(self):
        return {
            "name": self.name,
            "id": self.id,
            "type": self.type,
            "properties": self.param
        }
