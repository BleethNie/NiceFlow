import json
import random

import duckdb
import pandas as pd
from faker import Faker

from src.core.flow import Flow
from src.core.plugin import IPlugin


class FakerInput(IPlugin):

    def __init__(self):
        super().__init__()
        # 缓存编译字节码
        self.compile_dict = {}
        # 创建一个duckdb连接
        self.con = duckdb.connect()

    def init(self, param: json,flow:Flow):
        super(FakerInput, self).init(param,flow)
        #  编译字节码对象
        columns = self.param["columns"]
        for column in columns:
            exec_str = "faker.{}()".format(column)
            compile_obj = compile(exec_str, '', 'eval')
            self.compile_dict[column] = compile_obj

    def execute(self):
        rows = self.param["rows"]
        columns = self.param["columns"]
        randoms = self.param["randoms"]
        list_map = []
        # faker不能去掉，因为compile_obj为动态编译
        faker = Faker('zh-CN')
        for i in range(rows):
            current_row = {}
            for column in columns:
                compile_obj = self.compile_dict[column]
                value = eval(compile_obj)
                current_row[column] = value
            for element in randoms:
                key = element["key"]
                values = element["values"]
                value = random.choice(values)
                current_row[key] = value
            list_map.append(current_row)

        # 组装最后的结果
        df = pd.DataFrame(list_map)
        rel = self.con.from_df(df)
        # 设置下一步结果
        self.set_result(rel)

    def to_json(self):
        super(FakerInput, self).to_json()
