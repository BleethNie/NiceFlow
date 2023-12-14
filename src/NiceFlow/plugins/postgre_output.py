import json

from loguru import logger
import psycopg2

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin
from odps import ODPS
import pyarrow as pa
from sqlalchemy import create_engine


class PostgreOutput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(PostgreOutput, self).init(param, flow)


    def execute(self):
        super(PostgreOutput, self).execute()

        # param信息
        host = self.param.get("host","127.0.0.1")
        port = self.param.get("port",3306)
        db = self.param.get("db","")
        user = self.param.get("username","root")
        password = self.param.get("password","123456")
        table =  self.param.get("table","")
        id =  self.param.get("id","")

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        duck_df = self._pre_result_dict[pre_node.name]

        conn_string = f'postgresql://{user}:{password}@{host}:{port}/{db}'
        engine = create_engine(conn_string)
        conn = engine.connect()

        duck_df.to_df().to_sql(table,con=conn,chunksize=10000,if_exists='replace',index=False,index_label=id)


    def to_json(self):
        super(PostgreOutput, self).to_json()

    def close(self):
        super(PostgreOutput, self).close()
