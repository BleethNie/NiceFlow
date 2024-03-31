import json

import duckdb.duckdb

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
        super(CsvInput, self).execute()
        filename = self.param["filename"]
        header = self.param.get("header", True)
        all_varchar = self.param.get("all_varchar", None)
        compression = self.param.get("compression", "auto")
        delim = self.param.get("delim", ",")
        names = self.param.get("names", [])
        sample_size = self.param.get("sample_size", 20480)
        dtype = self.param.get("dtype", [])
        encoding = self.param.get("encoding", None)
        skip = self.param.get("skip", None)

        csv_df = duckdb.read_csv(name=filename, header=header, compression=compression, sep=delim, dtype=dtype,
                                 encoding=encoding, sample_size=sample_size, all_varchar=all_varchar,skiprows=skip, names=names)
        self.set_result(csv_df)

    def to_json(self):
        super(CsvInput, self).to_json()

    def close(self):
        super(CsvInput, self).close()
