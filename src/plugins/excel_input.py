import json

import duckdb
import pandas as pd

from src.core.flow import Flow
from src.core.plugin import IPlugin


class ExcelInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(ExcelInput, self).init(param, flow)

    def execute(self):
        file_name = self.param["file_name"]
        sheet_name = self.param["sheet_name"]
        df = pd.read_excel(file_name,sheet_name=sheet_name)
        excel_df = duckdb.from_df(df)
        self.set_result(excel_df)

    def to_json(self):
        super(ExcelInput, self).to_json()

    def close(self):
        super(ExcelInput, self).close()
