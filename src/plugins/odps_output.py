import json

from core.flow import Flow
from core.plugin import IPlugin
from odps import ODPS
import pandas as pd
import pyarrow as pa

class ODPSOutput(IPlugin):

    def init(self, param: json, flow: Flow):
        super().init(param, flow)


    def execute(self):
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]
        logger.debug(self.param)

        # param信息
        access_key = self.param["access_key"]
        access_secret = self.param.get("access_secret", "")
        project = self.param.get("project", "")
        end_point = self.param.get("end_point", "")
        partition = self.param.get("partition", "")
        table_name = self.param.get("table_name", "")
        odps = ODPS(access_key, access_secret,
                 project=project, endpoint=end_point)


        t = odps.get_table(table_name)
        with t.open_writer(partition=partition, create_partition=True, arrow=True) as writer:
            # 写入 RecordBatch
            batch = pa.RecordBatch.from_pandas(df)
            writer.write(batch)
            # 也可以直接写入 Pandas DataFrame
            writer.write(df)


    def to_json(self):
        super().to_json()

    def close(self):
        super().close()
