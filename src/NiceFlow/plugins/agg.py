import json

import duckdb

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin
from loguru import logger


class Agg(IPlugin):

    def init(self, param: json, flow: Flow):
        super(Agg, self).init(param, flow)

    def execute(self):
        super(Agg, self).execute()
        # param信息
        keys = self.param.get("keys")
        aggs = self.param.get("aggs")

        keys = ",".join(keys)

        res = ""
        for item in aggs:
            value = item["value"]
            a = item["agg"]
            res = res +f"{a}({value}),"
        res = res.removesuffix(",")


        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        duck_df = self._pre_result_dict[pre_node.name]
        sql_str = f"select {keys} , {res} from duck_df group by {keys} "
        logger.info(f"执行脚本为：{sql_str}" )
        result_df = duckdb.sql(sql_str)
        # 写入结果
        self.set_result(result_df)

    def to_json(self):
        super(Agg, self).to_json()
