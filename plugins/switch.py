import json

from core.plugin import IPlugin


class Switch(IPlugin):

    def init(self, param: json):
        super(Switch, self).init(param)

    def execute(self):
        self.param[""]
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]
        df.to_csv()

    def to_json(self):
        super(Switch, self).to_json()
