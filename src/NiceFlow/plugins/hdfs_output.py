import json
import os.path
import shutil

import duckdb
from hdfs import InsecureClient
from loguru import logger

from NiceFlow.core import tool
from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class HDFSOutput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(HDFSOutput, self).init(param, flow)

    def execute(self):
        super(HDFSOutput, self).execute()
        logger.debug(self.param)

        url = self.param.get("url", "http://127.0.0.1:9870")
        user = self.param.get("user", "hdfs")
        source = self.param.get("source", "")
        hdfs_path = self.param.get("dest", "")
        partitions = self.param.get("partitions", "")
        format = self.param.get("format", "parquet")
        columns = self.param.get("columns", "*")

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        duckdb_df = self._pre_result_dict[pre_node.name]
        temp_table = f"temp_{tool.random_str()}"
        duckdb_df.to_table(temp_table)

        is_dir = False
        partition_sql = ""
        if partitions is not None and partitions.strip():
            partition_sql = f",PARTITION_BY ({partitions})"
            is_dir = True

        if is_dir:
            if not os.path.exists(source):
                os.makedirs(source)
        else:
            parent_dir = os.path.dirname(source)
            logger.debug(f"parent_dir: {parent_dir}")
            if not os.path.exists(parent_dir) and parent_dir.strip():
                os.makedirs(parent_dir)

        # 数据导出到本地
        sql = f'''
        COPY (select {columns} from {temp_table} ) TO '{source}' (FORMAT {format} {partition_sql});
        '''
        logger.debug(f"执行sql: {sql}")
        duckdb.sql(sql)

        # 数据写入hdfs
        client = InsecureClient(f'{url}', user=user)
        logger.debug(f"source is {source}")

        client.upload(hdfs_path, source,overwrite=True)

        self.set_result(None)

    def to_json(self):
        super(HDFSOutput, self).to_json()

    def close(self):
        super(HDFSOutput, self).close()

        source = self.param.get("source", "")
        if os.path.exists(source):
            shutil.rmtree(source)
