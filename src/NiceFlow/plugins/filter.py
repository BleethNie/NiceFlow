import json

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class Filter(IPlugin):

    def init(self, param: json, flow: Flow):
        super().init(param, flow)

    def execute(self):
        super(Filter, self).execute()

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]
        df.filter()
        df.unique()

    def to_json(self):
        super().to_json()

    def close(self):
        super().close()
