import json

import duckdb
from loguru import logger
from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin
import akshare as ak


class Agg(IPlugin):

    def init(self, param: json, flow: Flow):
        super(Agg, self).init(param, flow)

    def execute(self):
        super(Agg, self).execute()
        # param信息
        key = self.param["key"]
        aggs = self.param.get("aggs")
        res = ""
        for item in aggs:
            value = item["value"]
            a = item["agg"]
            res = res +f"{a}({value}),"
        res = res.removesuffix(",")
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        duck_df = self._pre_result_dict[pre_node.name]

        result_df = duckdb.sql(f"select {key},{res} from duck_df group by {key} ")

        # 写入结果
        self.set_result(result_df)

    def to_json(self):
        super(Agg, self).to_json()
