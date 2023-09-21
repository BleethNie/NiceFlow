import json

from core.flow import Flow
from core.plugin import IPlugin


class CsvInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(CsvInput, self).init(param, flow)

    def execute(self):
        file_name = self.param["file_name"]
        csv_df = self.flow.con.read_csv(file_name)
        self.set_result(csv_df)

    def to_json(self):
        super(CsvInput, self).to_json()

    def close(self):
        super(CsvInput, self).close()
