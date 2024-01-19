import json

import duckdb

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class DuckDBOutput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(DuckDBOutput, self).init(param,flow)

    def execute(self):
        super(DuckDBOutput, self).execute()
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        my_df = self._pre_result_dict[pre_node.name]

        path = self.param["path"]
        table = self.param["table"]

        con = duckdb.connect(path)

        con.sql("CREATE TABLE {table_name} AS SELECT * FROM my_df".format(table_name=table))

        con.commit()

        self.set_result(None)


    def to_json(self):
        super(DuckDBOutput, self).to_json()
