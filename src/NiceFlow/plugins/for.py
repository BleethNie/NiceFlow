import json

import loguru

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class For(IPlugin):
    """
    将记录作为循环数据，一行记录循环一次，将行记录作为变量
    """

    def init(self, param: json, flow: Flow):
        super(For, self).init(param, flow)
        self.count = 0

    def execute(self):
        super(For, self).execute()

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]
        self.dict_result = df.to_df().to_dict(orient="records")

        row = self.dict_result[self.count]
        for k,v  in row.items():
            self.flow.param_dict["row.{}".format(k)] = v

        self.set_result(None)

    def to_json(self):
            super(For, self).to_json()
