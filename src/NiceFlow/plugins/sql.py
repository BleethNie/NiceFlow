import json

import duckdb
from loguru import logger

from NiceFlow.common.module_util import register_user_function, register_sys_function
from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class SQL(IPlugin):

    def init(self, param: json, flow: Flow):
        super(SQL, self).init(param, flow)
        self.con = duckdb.connect()
        # 注册系统函数
        register_sys_function(self.con)

    def execute(self):
        super(SQL, self).execute()

        function_paths = self.param.get("function_paths", [])
        for path in function_paths:
            register_user_function(path, self.con)

        sql = self.param["sql"]
        inputs = self.param["inputs"]

        # 获取上一步结果
        for input in inputs:
            step = input["step"]
            table = input["table"]
            logger.debug("{}-{}", table, step)
            duckdb.register(table, self._pre_result_dict[step].to_df())

        df = duckdb.sql(sql,connection=self.con).to_df()
        next_df = duckdb.from_df(df)
        self.set_result(next_df)

    def to_json(self):
        super(SQL, self).to_json()
