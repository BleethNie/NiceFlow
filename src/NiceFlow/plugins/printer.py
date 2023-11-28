import json

import loguru

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class Printer(IPlugin):

    def init(self, param: json, flow: Flow):
        super(Printer, self).init(param, flow)

    def execute(self):
        super(Printer, self).execute()

        # 打印日志
        msg = self.param.get("msg")
        loguru.logger.info(msg)

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]
        self.set_result(df)

    def to_json(self):
        super(Printer, self).to_json()
