import json

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class Console(IPlugin):

    def init(self, param: json, flow: Flow):
        super(Console, self).init(param, flow)

    def execute(self):
        super(Console, self).execute()
        row = self.param.get("row",10)
        max_col_width = self.param.get("max_col_width",10)
        max_width = self.param.get("max_width",800)

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        console_df = self._pre_result_dict[pre_node.name]
        console_df.limit(row).show(max_col_width=max_col_width,max_width=max_width)
        self.set_result(console_df)


    def to_json(self):
        super(Console, self).to_json()

    def close(self):
        super(Console, self).close()