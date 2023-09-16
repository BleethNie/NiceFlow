import json

import duckdb
import pandas as pd
from sqlalchemy import create_engine, text

from core.flow import Flow
from core.plugin import IPlugin


class MySQLInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(MySQLInput, self).init(param, flow)

    def execute(self):
        query = self.param["query"]
        host = self.param["host"]
        db = self.param["db"]
        user = self.param["user"]
        password = self.param["password"]
        port = self.param["port"]
        engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8'
                               % (user, password, host, port, db))
        connection = engine.connect()
        df = pd.read_sql_query(sql=text(query), con=connection)
        sql_df = duckdb.from_df(df)
        self.set_result(sql_df)

    def to_json(self):
        super(MySQLInput, self).to_json()

    def close(self):
        super(MySQLInput, self).close()
