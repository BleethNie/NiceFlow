import json

import duckdb
import pandas as pd

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin
from loguru import logger


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
        add_sql = ""
        replace_sql = ""
        for column in columns:
            field = column["field"]
            default = column.get("default", None)
            mapping_field = column.get("mapping_field", field)

            # 映射方式处理
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

            # 默认值处理
            if default is not None:
                replace_value = default
            else:
                replace_value = field

            # 是否替换原有列
            if mapping_field == field:
                new_field = field
                replace_sql = f"{replace_sql} function_mapping( {field}, '{replace_value}', map {mapping} ) as {new_field}"
            else:
                new_field = mapping_field
                add_sql = f"{add_sql} function_mapping( {field}, '{replace_value}', map {mapping} ) as {new_field}"

        add_sql = add_sql.removesuffix(",")
        replace_sql = replace_sql.removesuffix(",")

        final_sql = ""
        if replace_sql != "":
            final_sql = f"REPLACE ({replace_sql}) "
        if add_sql != "":
            final_sql = final_sql + f", {add_sql}"
        # 获取上一步结果
        pre_name = ""
        for pre_node in self.pre_nodes:
            if pre_node.name in step_map:
                continue
            else:
                pre_name = pre_node.name
        duck_df = self._pre_result_dict[pre_name]

        # 执行最后sql
        sql = f"select  * {final_sql} from duck_df"
        logger.info(f"执行SQL语句为 = {sql}")
        df = duckdb.execute(sql).fetch_df()
        result_df = duckdb.from_df(df)
        self.set_result(result_df)

    def to_json(self):
        super(Mapping, self).to_json()

    def close(self):
        super(Mapping, self).close()
