import json

import duckdb
import pandas as pd
from clickhouse_driver import Client

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class DB2Output(IPlugin):

    def init(self, param: json, flow: Flow):
        super(DB2Output, self).init(param, flow)

    def execute(self):
        super(DB2Output, self).execute()
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        duck_df = self._pre_result_dict[pre_node.name]
        # 写入结果
        self.set_result(duck_df)

    def to_json(self):
        super(DB2Output, self).to_json()
