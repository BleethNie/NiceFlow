import json

import duckdb

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class DuckDBInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(DuckDBInput, self).init(param,flow)

    def execute(self):
        super(DuckDBInput, self).execute()
        path = self.param.get("path","")
        sql = self.param.get("sql","")

        if path=="":
            duck_df = duckdb.sql(sql)
        else:
            con = duckdb.connect(path)
            df = duckdb.sql(sql,connection=con).to_df()
            duck_df = duckdb.from_df(df)
        self.set_result(duck_df)

    def to_json(self):
        super(DuckDBInput, self).to_json()
