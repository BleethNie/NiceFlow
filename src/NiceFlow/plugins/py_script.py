import json

import duckdb

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class PyScripy(IPlugin):


    def init(self, param: json,flow:Flow):
        super(PyScripy, self).init(param,flow)

    def execute(self):
        super(PyScripy, self).execute()
        con = duckdb.connect()

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        duck_df = self._pre_result_dict[pre_node.name]

        duck_df.show()


    def to_json(self):
        super(PyScripy, self).to_json()
