import json

import duckdb
import pandas as pd

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class CosOutput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(CosOutput, self).init(param, flow)

    def execute(self):
        super(CosOutput, self).execute()
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        duck_df = self._pre_result_dict[pre_node.name]
        # 写入结果
        self.set_result(duck_df)

    def to_json(self):
        super(CosOutput, self).to_json()
