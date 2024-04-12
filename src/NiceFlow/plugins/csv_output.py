import json

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class CsvOutput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(CsvOutput, self).init(param, flow)

    def execute(self):
        super(CsvOutput, self).execute()
        file_name = self.param["filename"]
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        duck_df = self._pre_result_dict[pre_node.name]
        df = duck_df.to_df()
        df.to_csv(file_name, index=False)

        self.set_result(None)

    def to_json(self):
        super(CsvOutput, self).to_json()
