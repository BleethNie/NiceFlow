import json

import duckdb
from loguru import logger
from sqlglot import select

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class Filter(IPlugin):

    def init(self, param: json, flow: Flow):
        super().init(param, flow)

    def execute(self):
        super(Filter, self).execute()

        where = self.param.get("condition","")

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]
        sql = select("*").from_("df").where(where).sql()
        logger.info("执行sql：{}",sql)
        result = duckdb.from_df(duckdb.sql(sql).df())
        self.set_result(result)


    def to_json(self):
        super().to_json()

    def close(self):
        super().close()
