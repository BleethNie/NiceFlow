import json

import duckdb
import pandas
from sqlalchemy import create_engine
from sqlalchemy.sql.expression import text

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class DuckDBInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(DuckDBInput, self).init(param,flow)

    def execute(self):
        super(DuckDBInput, self).execute()
        path = self.param["path"]
        sql = self.param["sql"]

        con = duckdb.connect(path)
        df = con.execute(sql).fetchdf()
        self.set_result(df)


    def to_json(self):
        super(DuckDBInput, self).to_json()
