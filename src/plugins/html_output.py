import json

from src.core.flow import Flow
from src.core.plugin import IPlugin


class HtmlOutput(IPlugin):

    def init(self, param: json,flow:Flow):
        super(HtmlOutput, self).init(param,flow)

    def execute(self):
        html_path = self.param["html_path"]
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]
        df.to_df().to_html(html_path)

    def to_json(self):
        super(HtmlOutput, self).to_json()
