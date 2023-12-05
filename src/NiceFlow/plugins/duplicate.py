import json

import duckdb

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class Duplicate(IPlugin):
    """
    保留重复值
    删除一条重复值
    删除所有重复值
    """

    def init(self, param: json,flow:Flow):
        super(Duplicate, self).init(param,flow)

    def execute(self):
        super(Duplicate, self).execute()

        duplicate_fields = self.param["duplicate_fields"]
        order_fields = self.param["order_fields"]
        order_type = self.param.get("order_type","DESC")

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        duplicate_df = self._pre_result_dict[pre_node.name]
        sql_template = '''
        SELECT * FROM (
            SELECT *,
            ROW_NUMBER() OVER (PARTITION BY {duplicate_fields} ORDER BY {order_fields} {order_type} ) AS rn
        FROM duplicate_df ) AS t  WHERE rn = 1;
        '''
        sql = sql_template.format(duplicate_fields=duplicate_fields,order_fields=order_fields,order_type=order_type)
        result_df = duckdb.execute(sql).fetch_df()
        duck_df = duckdb.from_df(result_df)

        # 写入结果
        self.set_result(duck_df)

def to_json(self):
        super(Duplicate, self).to_json()
