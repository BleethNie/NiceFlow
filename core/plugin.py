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

    # 在类里定义一个装饰器
    def timer(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            s_time = time.time()
            func(self, *args, **kwargs)
            e_time = time.time()
            diff = e_time - s_time
            print('【{}】插件执行耗时【{}】秒'.format(self.plugin, diff))

        return wrapper

    @timer
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
