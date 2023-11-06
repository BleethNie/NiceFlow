import json

from clickhouse_driver import Client
from pyarrow import RecordBatch

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin
from loguru import  logger

class CKOutput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(CKOutput, self).init(param, flow)

    def execute(self):
        super(CKOutput, self).execute()
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]
        logger.debug(self.param)

        # param信息
        host = self.param["host"]
        port = self.param.get("port", 9000)
        db = self.param["db"]
        user = self.param.get("user", "default")
        password = self.param.get("password", "")
        table = self.param.get("table", "")
        batch_size = self.param.get("batch_size", 100)

        # 配置数据库
        client = Client(host=host, port=port, database=db, user=user, password=password)
        # 批量写数据库
        total_count = len(df.to_df())
        rel = df.fetch_arrow_reader(batch_size)
        logger.info(f"总记录数据为 {total_count}")
        count = 0
        while True:
            batch: RecordBatch = rel.read_next_batch()
            sql = f'INSERT INTO {table}  VALUES '
            # 写数据库
            client.execute(sql, batch.to_pandas().to_dict(orient="records"), types_check=False)

            count = count + 1
            logger.debug(f"执行次数{count}")

            if total_count <= count * batch_size:
                break

    def to_json(self):
        super(CKOutput, self).to_json()
