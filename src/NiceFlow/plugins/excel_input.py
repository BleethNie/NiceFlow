import json

import duckdb
import pandas as pd

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class ExcelInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(ExcelInput, self).init(param, flow)

    def execute(self):
        super(ExcelInput, self).execute()

        file_name = self.param["file_name"]
        sheet_name = self.param.get("sheet_name", "")
        if len(sheet_name) == 0:
            df = pd.read_excel(file_name)
        else:
            df = pd.read_excel(file_name, sheet_name=sheet_name)
        excel_df = duckdb.from_df(df)
        self.set_result(excel_df)

    def to_json(self):
        super(ExcelInput, self).to_json()

    def close(self):
        super(ExcelInput, self).close()
