import json

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class HtmlOutput(IPlugin):

    def init(self, param: json,flow:Flow):
        super(HtmlOutput, self).init(param,flow)

    def execute(self):
        super(HtmlOutput, self).execute()

        filename = self.param["filename"]
        encoding = self.param.get("encoding","utf-8")
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]
        df.to_df().to_html(filename,index=False,encoding=encoding)

    def to_json(self):
        super(HtmlOutput, self).to_json()
