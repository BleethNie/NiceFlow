import json

import duckdb

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


# 空执行实际没有啥作用
class Rename(IPlugin):

    def init(self, param: json, flow: Flow):
        super(Rename, self).init(param, flow)

    def execute(self):
        super(Rename, self).execute()

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        duck_df = self._pre_result_dict[pre_node.name]
        # 需要修改名称的字段
        columns = self.param.get("columns",[])
        # 需要选择的字段
        selects = self.param.get("selects",[])
        # 需要排除的字段
        excludes = self.param.get("excludes",[])

        if len(selects)>0:
            duck_df = duck_df.select(selects)

        if len(excludes)>0:
            df = duck_df.to_df().drop(columns=excludes)
            duck_df = duckdb.from_df(df)

        if len(columns)>0:
            rename_dict = {}
            for column in columns:
                rename_dict[column["field"]] = column["rename"]
            df = duck_df.to_df().rename(rename_dict, axis=1)
            duck_df = duckdb.from_df(df)


        self.set_result(duck_df)

    def to_json(self):
        super(Rename, self).to_json()
