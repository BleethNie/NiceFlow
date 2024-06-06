import json

import duckdb
from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


# 从内存dataframe读取数据
class FrameInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(FrameInput, self).init(param, flow)

    def execute(self):
        super(FrameInput, self).execute()
        frame_name = self.param["frame_name"]

        # 写入结果
        frame:duckdb.DuckDBPyRelation = self.flow.get_result()[frame_name]
        self.set_result(frame)

    def to_json(self):
        super(FrameInput, self).to_json()
