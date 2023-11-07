import json

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class ParquetOutput(IPlugin):

    def init(self, param: json,flow:Flow):
        super(ParquetOutput, self).init(param,flow)

    def execute(self):
        super(ParquetOutput, self).execute()

        file_name = self.param["file_name"]
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]
        df.to_parquet(file_name)

        self.set_result(df)

    def to_json(self):
        super(ParquetOutput, self).to_json()
