import importlib
import inspect
import json

import duckdb
from NiceFlow.common.module_util import load_module
from loguru import logger

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class Function(IPlugin):

    def init(self, param: json, flow: Flow):
        super(Function, self).init(param, flow)
        self.con = duckdb.connect()

        # 注册系统函数
        module = importlib.import_module("NiceFlow.core.functions")
        items = inspect.getmembers(module, inspect.isfunction)
        for item in items:
            self.con.create_function(item[0], item[1])

    def execute(self):
        super(Function, self).execute()

        function_paths = self.param.get("function_paths",[])
        for path in function_paths:
            self.register_user_function(path)

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        pre_df = self._pre_result_dict[pre_node.name]
        pre_df = pre_df.to_df()
        table_columns = pre_df.columns

        sql = "select * "
        replace_sql = "REPLACE ( "
        as_sql = ""
        columns = self.param["columns"]
        for column in columns:
            key = column["key"]
            function = column["function"]
            if key in table_columns:
                replace_sql = replace_sql + f'{function} as {key}, '
            else:
                as_sql = as_sql + f"{function} as {key} , "
        if replace_sql != "REPLACE ( ":
            sql = f"{sql} {replace_sql.removesuffix(', ')}  {as_sql.removesuffix(', ')}) from pre_df"
        else:
            sql = sql + "," + as_sql.removesuffix(", ") + "from pre_df"

        logger.debug("sql = {}".format(sql))
        df = duckdb.sql(sql,connection=self.con).to_df()
        next_df = duckdb.from_df(df)
        self.set_result(next_df)

    def register_user_function(self,function_path):
        module = load_module(function_path)
        items = inspect.getmembers(module, inspect.isfunction)
        for item in items:
            self.con.create_function(item[0], item[1])
    def to_json(self):
        super(Function, self).to_json()

    def close(self):
        super(Function, self).close()
