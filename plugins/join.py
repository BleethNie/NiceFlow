import json

from core.flow import Flow
from core.plugin import IPlugin


class Join(IPlugin):

    def init(self, param: json,flow:Flow):
        super(Join, self).init(param,flow)

    def execute(self):
        # 获取上一步结果
        for index,pre_node in self.pre_nodes:
            df = self._pre_result_dict[pre_node.name]
        df.join()


    def to_json(self):
        super(Join, self).to_json()
