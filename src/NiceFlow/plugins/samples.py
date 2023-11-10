import json

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class Samples(IPlugin):
    """采样功能包括
    reservoir/基本采样 5   采样5条
    percent/百分比采样 10% 采样10%
    """

    def init(self, param: json, flow: Flow):
        super(Samples, self).init(param, flow)

    def execute(self):
        super(Samples, self).execute()

        sample_size = self.param.get("sample_size")

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        pre_df = self._pre_result_dict[pre_node.name]
        sample_df = pre_df.query("pre_df","select * from pre_df USING SAMPLE {};".format(sample_size))
        self.set_result(sample_df)

    def to_json(self):
        super(Samples, self).to_json()
