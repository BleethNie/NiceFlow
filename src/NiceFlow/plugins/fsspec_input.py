import json

import duckdb
from loguru import logger

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin
from fsspec import filesystem, available_protocols


class FSSpecInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(FSSpecInput, self).init(param, flow)

    def execute(self):
        super(FSSpecInput, self).execute()
        protocol = self.param.get("protocol", "")
        path = self.param.get("path", "")
        del self.param["path"]
        del self.param["protocol"]

        # 打印所有可用的协议
        print(available_protocols())
        duckdb.register_filesystem(filesystem(protocol,**self.param))
        sql = f"SELECT * FROM read_csv('{protocol}://{path}')"
        logger.info(f"执行的SQL = {sql}")
        duck_df = duckdb.sql(sql)
        self.set_result(duck_df)



    def to_json(self):
        super(FSSpecInput, self).to_json()

    def close(self):
        super(FSSpecInput, self).close()
