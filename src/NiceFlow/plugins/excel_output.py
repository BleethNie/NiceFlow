import json

from loguru import logger

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class ExcelOutput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(ExcelOutput, self).init(param, flow)

    def execute(self):
        super(ExcelOutput, self).execute()
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        duckdb_df = self._pre_result_dict[pre_node.name]
        logger.debug(self.param)

        file_name = self.param["file_name"]
        sheet_name = self.param.get("sheet_name", "")
        if sheet_name == "":
            duckdb_df.to_df().to_excel(file_name, index=False)
        else:
            duckdb_df.to_df().to_excel(file_name, sheet_name=sheet_name, index=False)
        self.set_result(None)

    def to_json(self):
        super(ExcelOutput, self).to_json()

    def close(self):
        super(ExcelOutput, self).close()
