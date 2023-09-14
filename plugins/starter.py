import json

import duckdb

from core.plugin import IPlugin


class Starter(IPlugin):

    def init(self, param: json):
        super(Starter, self).init(param)

    def execute(self):
        self.param[""]

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]
        res = duckdb.sql("SELECT * FROM tbl USING SAMPLE 10%;")



    def to_json(self):
        super(Starter, self).to_json()
