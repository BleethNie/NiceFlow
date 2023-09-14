import json

import duckdb

from core.plugin import IPlugin


class CsvInput(IPlugin):

    def init(self, param: json):
        super(CsvInput, self).init(param)

    def execute(self):
        file_name = self.param["file_name"]
        df = duckdb.read_csv(file_name)


    def to_json(self):
        super(CsvInput, self).to_json()
