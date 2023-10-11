import json

from src.core.flow import Flow
from src.core.plugin import IPlugin


class SubFlow(IPlugin):

    def init(self, param: json,flow:Flow):
        super(SubFlow, self).init(param,flow)

    def execute(self):
        flow_path = self.param("flow","")
        from src.core.manager import FlowManager
        myFlow: Flow = FlowManager.read(flow_path)
        myFlow.run()
        myFlow.close()

    def to_json(self):
        super(SubFlow, self).to_json()
