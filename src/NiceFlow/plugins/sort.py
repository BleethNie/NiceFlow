import json

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin
from loguru import  logger

class Sort(IPlugin):

    def init(self, param: json, flow: Flow):
        super(Sort, self).init(param, flow)

    def execute(self):
        super(Sort, self).execute()

        columns = self.param["columns"]
        order_exp = ""
        for column in columns:
            field = column["field"]
            sort = column["sort"]
            if sort is None:
                sort = "asc"
            order_exp = order_exp + ", {} {}".format(field, sort)
        order_exp = order_exp.removeprefix(",")
        logger.debug("order_exp = ",order_exp)
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]
        df = df.order(order_exp)
        self.set_result(df)


    def to_json(self):
        super(Sort, self).to_json()
