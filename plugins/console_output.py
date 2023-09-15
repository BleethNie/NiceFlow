import json

from core.flow import Flow
from core.plugin import IPlugin


class ConsoleOutput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(ConsoleOutput, self).init(param, flow)

    def execute(self):
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        console_df = self._pre_result_dict[pre_node.name]
        print(type(console_df))
        print(console_df)

    def to_json(self):
        super(ConsoleOutput, self).to_json()

    def close(self):
        super(ConsoleOutput, self).close()