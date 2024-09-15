import json

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class MarkdownOutput(IPlugin):

    def __init__(self):
        super().__init__()

    def init(self, param: json, flow: Flow):
        super(MarkdownOutput, self).init(param, flow)

    def execute(self):
        super(MarkdownOutput, self).execute()

        file_path = self.param.get("filename")
        limit = self.param.get("limit", 1000)
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]
        df.limit(limit).to_df().to_markdown(file_path,index=False)

    def to_json(self):
        super(MarkdownOutput, self).to_json()
