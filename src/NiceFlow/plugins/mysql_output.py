import json

from sqlalchemy import create_engine

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class MySQLOutput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(MySQLOutput, self).init(param,flow)

    def execute(self):
        super(MySQLOutput, self).execute()

        host = self.param.get("host","127.0.0.1")
        port = self.param.get("port",3306)
        db = self.param.get("db","")
        user = self.param.get("user","root")
        password = self.param.get("password","123456")
        table =  self.param.get("table","")
        id =  self.param.get("id","")

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        duck_df = self._pre_result_dict[pre_node.name]

        # 写数据库
        engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8'
                               % (user, password, host, port, db))
        duck_df.to_df().to_sql(table,con=engine,chunksize=10000,if_exists='replace',index=False,index_label=id)


    def to_json(self):
        super(MySQLOutput, self).to_json()
