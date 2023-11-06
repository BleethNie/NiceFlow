import json

import duckdb

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin
from loguru import  logger


def function_mask(x: str, start: int, length: int, sign: str) -> str:
    start_str = x[:start]
    end_str = x[start + length:]
    sign_str = sign * length
    return start_str + sign_str + end_str


class Masking(IPlugin):

    def init(self, param: json, flow: Flow):
        super(Masking, self).init(param, flow)
        duckdb.create_function('function_mask', function_mask)

    def execute(self):
        super(Masking, self).execute()

        columns = self.param["columns"]
        column = columns[0]
        field = column["field"]
        startIndex = column["startIndex"]
        length = column["length"]
        sign = column["sign"]

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]

        sql = "select *,function_mask( {} ,{},{},'{}') as {}_mask from df" \
            .format(field, startIndex, length, sign, field)
        logger.debug("sql = {}".format(sql))
        df = duckdb.from_df(duckdb.sql(sql).df())
        self.set_result(df)

    def to_json(self):
        super(Masking, self).to_json()

    def close(self):
        super(Masking, self).close()
        duckdb.remove_function("function_mask")
