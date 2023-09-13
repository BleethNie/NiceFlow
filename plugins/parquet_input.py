import json

import duckdb

from core.plugin import IPlugin


class ParquetInput(IPlugin):

    def init(self, param: json):
        super(ParquetInput, self).init(param)

    def execute(self):
        file_name = self.param["file_name"]
        df = duckdb.read_parquet(file_name)
        # 设置结果
        for node in self.next_nodes:
            node.set_result(self.name, df)
        # 执行下一步
        for node in self.next_nodes:
            node.execute()

    def to_json(self):
        super(ParquetInput, self).to_json()
