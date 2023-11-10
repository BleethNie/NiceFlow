import json

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class UnPivot(IPlugin):

    def init(self, param: json,flow:Flow):
        super(UnPivot, self).init(param,flow)

    def execute(self):
        super(UnPivot, self).execute()

        self.param[""]
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        pre_df = self._pre_result_dict[pre_node.name]
        self.set_result(pre_df)

    def to_json(self):
        super(UnPivot, self).to_json()
