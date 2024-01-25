import json

import duckdb
import loguru
import pandas as pd
import pymysql
from sqlalchemy import create_engine, text

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class MySQLInput(IPlugin):

    def __init__(self):
        super().__init__()
        self.connection = None

    def init(self, param: json, flow: Flow):
        super(MySQLInput, self).init(param, flow)


    def execute(self):
        super(MySQLInput, self).execute()

        query = self.param.get("query", "")
        host = self.param.get("host", "127.0.0.1")
        port = self.param.get("port", 3306)
        db = self.param.get("db", "")
        user = self.param.get("username", "root")
        password = self.param.get("password", "123456")
        mode = self.param.get("mode", "cursor")
        if mode == "cursor":
            # 连接数据库
            self.connection = pymysql.connect(host=host, user=user, db=db,
                                      password=password, port=port, charset='utf8mb4')
            cursor = self.connection.cursor()
            loguru.logger.debug(f"执行query = {query}")
            cursor.execute(query)
            # 获取表头
            des_list = cursor.description
            column_list = [desc[0] for desc in des_list]
            # 获取数据
            row_list = []
            while True:
                row = cursor.fetchone()
                if row is None:
                    break
                row_list.append(row)
            # 组装得到结果
            df = pd.DataFrame(columns=column_list, data=row_list)
            sql_df = duckdb.from_df(df)
            self.set_result(sql_df)
        else:
            engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8mb4'
                                   % (user, password, host, port, db))
            self.connection = engine.connect()
            df = pd.read_sql_query(sql=text(query), con=self.connection)
            sql_df = duckdb.from_df(df)
            self.set_result(sql_df)

    def to_json(self):
        super(MySQLInput, self).to_json()

    def close(self):
        super(MySQLInput, self).close()
        if self.connection is not None:
            self.connection.close()
