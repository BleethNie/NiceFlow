import json

import duckdb

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin
from loguru import  logger

# 空执行实际没有啥作用
class SQL(IPlugin):

    def init(self, param: json, flow: Flow):
        super(SQL, self).init(param, flow)

    def execute(self):
        sql = self.param["sql"]
        inputs = self.param["inputs"]

        # 获取上一步结果

        for input in inputs:
            step = input["step"]
            table = input["table"]
            logger.debug(table,step)
            duckdb.register(table, self._pre_result_dict[step].to_df())
        result_df = duckdb.sql(sql)
        # 写入结果
        self.set_result(result_df)


    def to_json(self):
        super(SQL, self).to_json()
