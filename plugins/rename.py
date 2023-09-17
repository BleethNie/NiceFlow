import json

import duckdb
import pandas as pd

from core.flow import Flow
from core.plugin import IPlugin


# 空执行实际没有啥作用
class Rename(IPlugin):

    def init(self, param: json, flow: Flow):
        super(Rename, self).init(param, flow)

    def execute(self):
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]

        columns = self.param["columns"]
        rename_dict = {}
        for column in columns:
            rename_dict[column["field"]] = column["rename"]
        df = df.to_df().rename(rename_dict, axis=1)
        df = duckdb.from_df(df)
        self.set_result(df)

    def to_json(self):
        super(Rename, self).to_json()
