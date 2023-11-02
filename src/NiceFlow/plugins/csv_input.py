import json

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class StringConverter(dict):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return str

    def get(self, default=None):
        return str


class CsvInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(CsvInput, self).init(param, flow)

    def execute(self):
        file_name = self.param["file_name"]
        csv_df = self.flow.con.read_csv(file_name,header=True)
        self.set_result(csv_df)

    def to_json(self):
        super(CsvInput, self).to_json()

    def close(self):
        super(CsvInput, self).close()
