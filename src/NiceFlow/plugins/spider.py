import json

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class Spider(IPlugin):


    def init(self, param: json, flow: Flow):
        super(Spider, self).init(param, flow)
        self.count = 1

    def execute(self):
        super(Spider, self).execute()

        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]
        self.dict_result = df.to_df().to_dict(orient="records")

        if self.count == len(self.dict_result)+2:
            return

        if self.count == len(self.dict_result)+1:
            self.set_result(df)
            return

        row = self.dict_result[self.count-1]
        for k, v in row.items():
            self.flow.param_dict["row.{}".format(k)] = v

        self.set_result(df)

    def to_json(self):
        super(Spider, self).to_json()
