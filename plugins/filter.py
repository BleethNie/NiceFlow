import json

from core.flow import Flow
from core.plugin import IPlugin


class HttpOutput(IPlugin):

    def init(self, param: json, flow: Flow):
        super().init(param, flow)


    def execute(self):
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]
        df.unique()

    def to_json(self):
        super().to_json()

    def close(self):
        super().close()
