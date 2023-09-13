import json

from core.plugin import IPlugin


class ParquetOutput(IPlugin):

    def init(self, param: json):
        super(ParquetOutput, self).init(param)

    def execute(self):
        file_name = self.param["file_name"]
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]
        df.to_parquet(file_name)

    def to_json(self):
        super(ParquetOutput, self).to_json()
