import json

from core.plugin import IPlugin


class CsvOutput(IPlugin):

    def init(self, param: json):
        super(CsvOutput, self).init(param)

    def execute(self):
        self.param[""]
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]
        df.to_csv()


    def to_json(self):
        super(CsvOutput, self).to_json()
