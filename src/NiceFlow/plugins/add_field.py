import importlib
import inspect
import json

import duckdb
from loguru import logger

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class AddField(IPlugin):

    def init(self, param: json, flow: Flow):
        super(AddField, self).init(param, flow)
        self.con = duckdb.connect()

        # 注册函数
        module = importlib.import_module("NiceFlow.core.functions")
        items = inspect.getmembers(module, inspect.isfunction)
        for item in items:
            self.con.create_function(item[0], item[1])

    def execute(self):
        super(AddField, self).execute()

        sql = "select *, "
        columns = self.param["columns"]
        for column in columns:
            key = column["key"]
            function = column["function"]
            sql = sql + f"{function} as {key}, "
        sql = sql.removesuffix(", ") + " from df"

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]

        logger.debug("sql = {}".format(sql))
        df = duckdb.from_df(self.con.sql(sql).df())
        self.set_result(df)

    def to_json(self):
        super(AddField, self).to_json()

    def close(self):
        super(AddField, self).close()
