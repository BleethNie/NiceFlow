import json

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class CosInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(CosInput, self).init(param, flow)

    def execute(self):
        super(CosInput, self).execute()
        # 写入结果
        self.set_result()

    def to_json(self):
        super(CosInput, self).to_json()
