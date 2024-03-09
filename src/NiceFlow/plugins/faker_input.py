import json
import random

import duckdb
import pandas as pd
from faker import Faker

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class FakerInput(IPlugin):

    def __init__(self):
        super().__init__()

    def init(self, param: json, flow: Flow):
        super(FakerInput, self).init(param, flow)

    def execute(self):
        super(FakerInput, self).execute()
        rows = self.param["rows"]
        columns = self.param.get("columns", [])
        randoms = self.param.get("randoms", [])

        faker = Faker('zh-CN')
        result = {}
        for column in columns:
            faker_generator = getattr(faker, column)
            result[column] = [faker_generator() for _ in range(rows)]

        for element in randoms:
            key = element["key"]
            values = element["values"]
            result[key] = [random.choice(values) for _ in range(rows)]

        # 组装最后的结果
        df = pd.DataFrame(result)
        duck_df = duckdb.from_df(df)
        # 设置下一步结果
        self.set_result(duck_df)

    def to_json(self):
        super(FakerInput, self).to_json()
