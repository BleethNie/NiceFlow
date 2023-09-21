import json

import duckdb

from core.flow import Flow
from core.plugin import IPlugin


def function_mapping(field: str, default: str, mapping: dict) -> str:
    keys = mapping["key"]
    values = mapping["value"]
    mapping = {}
    for index, key in enumerate(keys):
        mapping[key] = values[index]
    if field in mapping:
        return mapping[field]
    return default


class Mapping(IPlugin):

    def init(self, param: json, flow: Flow):
        super(Mapping, self).init(param, flow)
        duckdb.create_function('function_mapping', function_mapping)

    def execute(self):
        columns = self.param["columns"]
        field_sql = ""
        for column in columns:
            field = column["field"]
            default = column.get("default",None)
            mapping = column["mapping"]
            if default is not None:
                field_sql = field_sql + "function_mapping( {},'{}',map {} ) as {}_mapping , " \
                    .format(field, default, mapping, field)
            if default is None:
                field_sql = field_sql + "function_mapping( {},{},map {} ) as {}_mapping ," \
                    .format(field, field, mapping, field)
        field_sql = field_sql.removesuffix(",")
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]

        sql = "select *,{} from df".format(field_sql)
        print("sql = {}".format(sql))
        df = duckdb.from_df(duckdb.sql(sql).df())
        self.set_result(df)

    def to_json(self):
        super(Mapping, self).to_json()

    def close(self):
        super(Mapping, self).close()
        duckdb.remove_function("function_mapping")
