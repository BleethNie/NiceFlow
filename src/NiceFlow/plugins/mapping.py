import json

import duckdb
import pandas as pd

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin
from loguru import  logger

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
        super(Mapping, self).execute()

        step_map = {}

        columns = self.param["columns"]
        field_sql = ""
        for column in columns:
            field = column["field"]
            default = column.get("default",None)
            if "plugin_mapping" in column:
                plugin_mapping = column["plugin_mapping"]
                step_name = plugin_mapping["step_name"]
                key_field = plugin_mapping["key_field"]
                value_field = plugin_mapping["value_field"]
                step_map[step_name] = 1
                temp_df = self._pre_result_dict[step_name].to_df()
                mapping = pd.Series(temp_df[value_field].values, index=temp_df[key_field]).to_dict()
                print(mapping)
            else:
                mapping = column["value_mapping"]
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
        mapping_df = duckdb.from_df(duckdb.sql(sql).df())
        self.set_result(mapping_df)

    def to_json(self):
        super(Mapping, self).to_json()

    def close(self):
        super(Mapping, self).close()
