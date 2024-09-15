import json

import duckdb.duckdb

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class JsonOutput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(JsonOutput, self).init(param, flow)

    def execute(self):
        super(JsonOutput, self).execute()
        filename = self.param["filename"]
        orient = self.param.get("orient","records")
        force_ascii = self.param.get("force_ascii",False)
        lines = self.param.get("lines",False)
        indent = self.param.get("indent",None)

        pre_node = self.pre_nodes[0]
        pre_df = self._pre_result_dict[pre_node.name]

        pre_df.to_df().to_json(filename,orient=orient, lines=lines,force_ascii=force_ascii,index=indent)

    def to_json(self):
        super(JsonOutput, self).to_json()

    def close(self):
        super(JsonOutput, self).close()
