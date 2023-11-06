import json

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class Duplicate(IPlugin):

    def init(self, param: json,flow:Flow):
        super(Duplicate, self).init(param,flow)

    def execute(self):
        super(Duplicate, self).execute()

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]


    def to_json(self):
        super(Duplicate, self).to_json()
