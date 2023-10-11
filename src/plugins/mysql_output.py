import json

from sqlalchemy import create_engine

from src.core.flow import Flow
from src.core.plugin import IPlugin


class MySQLOutput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(MySQLOutput, self).init(param,flow)

    def execute(self):
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]

        # 写数据库
        engine = create_engine('doris://root:xxx@localhost:9030/hive_catalog.hive_db')
        df.to_sql('table_name',con=engine,chunksize=10000,if_exists='replace',index=True,index_label='id_name')


    def to_json(self):
        super(MySQLOutput, self).to_json()
