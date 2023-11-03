import json

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class ConsoleOutput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(ConsoleOutput, self).init(param, flow)

    def execute(self):
        super(ConsoleOutput, self).execute()
        row = int(self.param["row"])
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        console_df = self._pre_result_dict[pre_node.name]
        console_df.limit(row).show()
        self.set_result(console_df)


    def to_json(self):
        super(ConsoleOutput, self).to_json()

    def close(self):
        super(ConsoleOutput, self).close()