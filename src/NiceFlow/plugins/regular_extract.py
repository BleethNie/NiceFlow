import json

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class RegularExtract(IPlugin):

    def init(self, param: json,flow:Flow):
        super(RegularExtract, self).init(param,flow)

    def execute(self):
        super(RegularExtract, self).execute()

        # 获取上一步结果
        for index,pre_node in self.pre_nodes:
            df = self._pre_result_dict[pre_node.name]
        df.join()


    def to_json(self):
        super(RegularExtract, self).to_json()
