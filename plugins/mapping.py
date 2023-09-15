import json
from sanic import Sanic, text, Config

import duckdb
import pandas as pd

from core.flow import Flow
from core.plugin import IPlugin


def function_mapping(x: str, start: int, length: int, sign: str) -> str:
    start_str = x[:start]
    end_str = x[start + length:]
    sign_str = sign * length
    return start_str + sign_str + end_str


class Mapping(IPlugin):

    def init(self, param: json, flow: Flow):
        super(Mapping, self).init(param, flow)
        duckdb.create_function('function_mapping', function_mapping)

    def execute(self):
        columns = self.param["columns"]
        column = columns[0]
        field = column["field"]
        startIndex = column["startIndex"]
        length = column["length"]
        sign = column["sign"]

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]

        sql = "select *,function_mapping( {} ,{},{},'{}') as {}_mask from df" \
            .format(field, startIndex, length, sign, field)
        print("sql = {}".format(sql))
        df = duckdb.from_df(duckdb.sql(sql).df())
        self.set_result(df)

    def to_json(self):
        super(Mapping, self).to_json()

    def close(self):
        super(Mapping, self).close()
        duckdb.remove_function("function_mapping")