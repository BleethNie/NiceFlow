import json

import duckdb
import pandas as pd
from clickhouse_driver import Client

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class DB2Input(IPlugin):

    def init(self, param: json, flow: Flow):
        super(DB2Input, self).init(param, flow)

    def execute(self):
        super(DB2Input, self).execute()
        # 写入结果
        self.set_result()

    def to_json(self):
        super(DB2Input, self).to_json()
