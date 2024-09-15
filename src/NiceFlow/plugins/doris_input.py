import uuid

from pydoris.doris_client import *

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class DorisInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(DorisInput, self).init(param, flow)

    def execute(self):
        super(DorisInput, self).execute()
        self.set_result(None)

    def to_json(self):
        super(DorisInput, self).to_json()

