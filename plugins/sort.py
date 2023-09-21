import json

from core.flow import Flow
from core.plugin import IPlugin


class Sort(IPlugin):

    def init(self, param: json, flow: Flow):
        super(Sort, self).init(param, flow)

    def execute(self):
        columns = self.param["columns"]
        order_exp = ""
        for column in columns:
            field = column["field"]
            sort = column["sort"]
            if sort is None:
                sort = "asc"
            order_exp = order_exp + ", {} {}".format(field, sort)
        order_exp = order_exp.removeprefix(",")

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]
        df = df.order(order_exp)
        self.set_result(df)


    def to_json(self):
        super(Sort, self).to_json()
