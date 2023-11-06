import json

import duckdb

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class ParquetInput(IPlugin):

    def init(self, param: json,flow:Flow):
        super(ParquetInput, self).init(param,flow)

    def execute(self):
        super(ParquetInput, self).execute()

        file_name = self.param["file_name"]
        df = duckdb.read_parquet(file_name)
        # 设置下一步结果
        self.set_result(df)

    def to_json(self):
        super(ParquetInput, self).to_json()
