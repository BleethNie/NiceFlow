import json

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class For(IPlugin):

    def init(self, param: json,flow:Flow):
        super(For, self).init(param,flow)

    def execute(self):
        super(For, self).execute()

        self.param[""]
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]
        df.to_csv()

    def to_json(self):
        super(For, self).to_json()
