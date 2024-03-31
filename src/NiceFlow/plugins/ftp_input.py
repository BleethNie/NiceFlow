import json

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class FtpInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(FtpInput, self).init(param, flow)

    def execute(self):
        super(FtpInput, self).execute()
        # param信息
        host = self.param["host"]
        port = self.param.get("port", 21)
        user = self.param.get("username", "default")
        password = self.param.get("password", "")


        # 写入结果
        self.set_result(ck_df)

    def to_json(self):
        super(FtpInput, self).to_json()

