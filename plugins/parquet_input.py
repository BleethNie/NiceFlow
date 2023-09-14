import json

import duckdb

from core.plugin import IPlugin


class ParquetInput(IPlugin):

    def init(self, param: json):
        super(ParquetInput, self).init(param)

    def execute(self):
        file_name = self.param["file_name"]
        df = duckdb.read_parquet(file_name)
        # 设置下一步结果
        self.set_result(df)

    def to_json(self):
        super(ParquetInput, self).to_json()
