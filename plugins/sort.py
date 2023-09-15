import json

from core.plugin import IPlugin


class Sort(IPlugin):

    def init(self, param: json):
        super(Sort, self).init(param)

    def execute(self):
        columns = self.param["columns"]
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]




    def to_json(self):
        super(Sort, self).to_json()
