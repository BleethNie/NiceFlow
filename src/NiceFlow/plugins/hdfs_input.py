import json

from hdfs import InsecureClient
from loguru import logger

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class HDFSInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(HDFSInput, self).init(param, flow)

    def execute(self):
        super(HDFSInput, self).execute()

        url = self.param.get("url", "http://127.0.0.1:9870")
        user = self.param.get("user", "hdfs")
        source = self.param.get("source", "")
        dest = self.param.get("dest", "")
        partitions = self.param.get("partitions", "")
        format = self.param.get("format", "parquet")
        columns = self.param.get("columns", "*")

        # 数据写入hdfs
        client = InsecureClient(f'{url}', user=user)
        logger.debug(f"source is {source}")
        client.download(source, dest)



    def to_json(self):
        super(HDFSInput, self).to_json()

    def close(self):
        super(HDFSInput, self).close()
