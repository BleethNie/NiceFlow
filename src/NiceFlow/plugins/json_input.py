import json

import duckdb.duckdb

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin



class JsonInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(JsonInput, self).init(param, flow)

    def execute(self):
        super(JsonInput, self).execute()
        filename = self.param["filename"]
        columns = self.param.get("columns", None)
        format = self.param.get("format", None)
        records = self.param.get("records", None)

        json_df = duckdb.read_json(name=filename, columns=columns, format=format, records=records)
        self.set_result(json_df)

    def to_json(self):
        super(JsonInput, self).to_json()

    def close(self):
        super(JsonInput, self).close()
