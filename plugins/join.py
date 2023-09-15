import json

from core.plugin import IPlugin


class Join(IPlugin):

    def init(self, param: json):
        super(Join, self).init(param)

    def execute(self):
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]


    def to_json(self):
        super(Join, self).to_json()
