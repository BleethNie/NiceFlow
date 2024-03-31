import json

import duckdb

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class Pivot(IPlugin):

    def init(self, param: json,flow:Flow):
        super(Pivot, self).init(param,flow)

    def execute(self):
        super(Pivot, self).execute()
        # PIVOT Cities ON Year USING sum(Population);
        key = self.param["key"]
        value = self.param["value"]
        agg = self.param["agg"]

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        duck_df = self._pre_result_dict[pre_node.name]
        result_df = duckdb.sql(f"PIVOT duck_df ON {key} USING by {agg}({value}) ")
        self.set_result(result_df)

    def to_json(self):
        super(Pivot, self).to_json()
