import json

import duckdb.duckdb

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin



class SplitFieldToRowsInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(SplitFieldToRowsInput, self).init(param, flow)

    def execute(self):
        super(SplitFieldToRowsInput, self).execute()
        column = self.param.get("column", None)
        split = self.param.get("split", ",")
        # mode = override[覆盖原字段]、new[生成新字段]
        mode = self.param.get("mode", "override")
        new_column = self.param.get("new_column", f"new_{column}")

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        pre_df = self._pre_result_dict[pre_node.name]

        sql = f"SELECT *,unnest(string_split({column},'{split}')) as {new_column}  from  pre_df;"
        duckdb_df = duckdb.sql(sql)
        self.set_result(duckdb_df)

    def to_json(self):
        super(SplitFieldToRowsInput, self).to_json()

