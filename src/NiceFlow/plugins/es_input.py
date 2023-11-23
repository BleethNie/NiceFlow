import json

import duckdb
import pandas as pd
from clickhouse_driver import Client

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class ESInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(ESInput, self).init(param, flow)

    def execute(self):
        super(ESInput, self).execute()
        # param信息
        host = self.param["host"]
        port = self.param.get("port", 9000)
        db = self.param["db"]
        user = self.param.get("user", "default")
        password = self.param.get("password", "")
        table = self.param.get("table", "")
        sql = self.param.get("sql", "")

        # 配置数据库
        client = Client(host=host, port=port, database=db, user=user, password=password)

        # 读取数据
        data,columns = client.execute(sql,with_column_types=True)
        real_columns = [item[0] for item in columns]
        df = pd.DataFrame(data,columns=real_columns)
        ck_df = duckdb.from_df(df)
        # 写入结果
        self.set_result(ck_df)

    def to_json(self):
        super(ESInput, self).to_json()
