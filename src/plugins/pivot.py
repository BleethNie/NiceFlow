import json

from src.core.flow import Flow
from src.core.plugin import IPlugin


class Pivot(IPlugin):

    def init(self, param: json,flow:Flow):
        super(Pivot, self).init(param,flow)

    def execute(self):
        self.param[""]
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        pre_df = self._pre_result_dict[pre_node.name]
        self.set_result(pre_df)

    def to_json(self):
        super(Pivot, self).to_json()
