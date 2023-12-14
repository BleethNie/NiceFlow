import json

import duckdb
import pandas as pd
from sqlalchemy import create_engine, text

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class DBExecute(IPlugin):

    def init(self, param: json, flow: Flow):
        super(DBExecute, self).init(param, flow)

    def execute(self):
        super(DBExecute, self).execute()

        query = self.param.get("query","")
        host = self.param.get("host","127.0.0.1")
        port = self.param.get("port",3306)
        db = self.param.get("db","")
        user = self.param.get("username","root")
        password = self.param.get("password","123456")
        engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8'
                               % (user, password, host, port, db))
        connection = engine.connect()
        connection.execute(query)

        self.set_result(None)

    def to_json(self):
        super(DBExecute, self).to_json()

    def close(self):
        super(DBExecute, self).close()
