import json

from core.flow import Flow
from core.plugin import IPlugin


class CsvOutput(IPlugin):

    def init(self, param: json,flow:Flow):
        super(CsvOutput, self).init(param,flow)

    def execute(self):
        file_name = self.param["file_name"]
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        duck_df = self._pre_result_dict[pre_node.name]
        df = duck_df.to_df()
        df.to_csv(file_name,index=False)


    def to_json(self):
        super(CsvOutput, self).to_json()
