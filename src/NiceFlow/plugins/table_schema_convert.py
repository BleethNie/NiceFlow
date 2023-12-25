import json

import duckdb
import pandas as pd

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class TableSchemaConvert(IPlugin):

    def init(self, param: json, flow: Flow):
        super(TableSchemaConvert, self).init(param, flow)
        self.data_type_dict = {"时间日期型": "TIMESTAMP(0)", "浮点型": "numeric(18,2)", "整型": "INT4", "布尔型": "INT4"}

    def execute(self):
        super(TableSchemaConvert, self).execute()

        table_field = self.param["table_field"]
        table_cn = self.param["table_cn"]
        comment_field = self.param["comment_field"]
        field = self.param["field"]
        data_type = self.param["data_type"]
        length = self.param["length"]
        condition = self.param["condition"]

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        duck_df = self._pre_result_dict[pre_node.name]

        # 聚合
        grouped = duck_df.to_df().groupby(table_field)
        result_list = []
        # 聚合内容进行循环
        for name, group in grouped:
            table_sql = f"CREATE TABLE  \"{name}\" (\n"
            comment_sql = "\n"
            table_name_cn = ""
            for index, row in group.iterrows():
                if index == 1:
                    table_name_cn = row[table_cn]
                comment_str = row[comment_field]
                condition_str = "NULL"
                if row[condition] == "M":
                    condition_str = "NOT NULL"

                data_type_str = row[data_type]
                if row[data_type] == "字符型":
                    data_type_str = f"VARCHAR({row[length]})"
                if row[data_type] in self.data_type_dict:
                    data_type_str = self.data_type_dict[row[data_type]]
                line = f"  \"{row[field]}\"  {data_type_str}  {condition_str},\n"
                table_sql = table_sql + line

                comment_line = f"COMMENT ON COLUMN \"{name}\".\"{row[field]}\" IS '{comment_str}';\n"
                comment_sql = comment_sql + comment_line

            table_sql = table_sql.removesuffix(",\n") + "\n"
            table_sql = table_sql + ");\n"

            comment_sql = comment_sql + "\n"

            table_comment_sql = f"COMMENT ON TABLE \"{name}\" IS '{table_name_cn}';"

            table_sql = table_sql+ table_comment_sql+comment_sql
            # 形成新记录
            result_list.append({"table_cn": table_name_cn, "table_name": name, "table_sql": table_sql})
        # 输出
        df = pd.DataFrame(result_list)
        self.set_result(duckdb.from_df(df))

    def to_json(self):
        super(TableSchemaConvert, self).to_json()
