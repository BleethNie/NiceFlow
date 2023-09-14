import json
import random

import duckdb
import pandas as pd
from faker import Faker

from core.plugin import IPlugin



class FakerInput(IPlugin):

    def init(self, param: json):
        super(FakerInput, self).init(param)
        # 创建一个duckdb连接
        self.con = duckdb.connect()

        # 缓存编译字节码
        self.compile_dict = {}
        #  编译字节码对象
        columns = self.param["columns"]
        faker = Faker('zh-CN')
        for column in columns:
            exec_str = "faker.{}()".format(column)
            compile_obj = compile(exec_str, '', 'eval')
            self.compile_dict[column] = compile_obj

    def execute(self):
        rows = self.param["rows"]
        columns = self.param["columns"]
        randoms = self.param["randoms"]
        list_map = []
        faker = Faker('zh-CN')
        for i in range(rows):
            current_row = {}
            for column in columns:
                compile_obj = self.compile_dict[column]
                value = eval(compile_obj)
                current_row[column] =value
            for element in randoms:
                key = element["key"]
                values = element["values"]
                value = random.choice(values)
                current_row[key] = value
            list_map.append(current_row)

        # 组装最后的结果
        df = pd.DataFrame(list_map)
        rel = self.con.from_df(df)

        # 设置结果
        for node in self.next_nodes:
            node.set_result(self.name, rel)
        # 执行下一步
        for node in self.next_nodes:
            node.execute()

    def to_json(self):
        super(FakerInput, self).to_json()
