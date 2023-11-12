import json

import duckdb
import pandas as pd
from sqlalchemy import create_engine, text

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class MySQLInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(MySQLInput, self).init(param, flow)

    def execute(self):
        super(MySQLInput, self).execute()

        query = self.param["query"]
        host = self.param.get("host","127.0.0.1")
        port = self.param.get("port",3306)
        db = self.param["db"]
        user = self.param.get("user","root")
        password = self.param.get("password","123456")
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
