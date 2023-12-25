import json

import pandas as pd
import sqlalchemy

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class OracleInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(OracleInput, self).init(param, flow)

    def execute(self):
        super(OracleInput, self).execute()

        # param信息
        username = self.param["username"]
        password = self.param["password"]
        host = self.param.get("host", "127.0.0.1")
        db = self.param.get("db", "")
        port = self.param.get("port", 1521)
        sid = self.param.get("sid", "ORCL")
        sql = self.param["sql"]
        table = self.param["table"]

        DATABASE = "DB"
        username = "DEV"
        PASSWORD = "password"
        conn_str = f"oracle://{username}:{password}@{DATABASE}"
        con = sqlalchemy.create_engine(conn_str)

        TABLENAME = "SEVERITY_CDFS"
        SQL  = "SELECT * FROM {}".format(TABLENAME)
        cdfs = pd.read_sql_query(SQL, con=con)
        # 写入结果
        self.set_result(None)

    def to_json(self):
        super(OracleInput, self).to_json()

    def close(self):
        super(OracleInput, self).close()
        self.con.close()
