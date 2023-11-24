import json

import duckdb
import loguru

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class For(IPlugin):
    """
    将记录作为循环数据，一行记录循环一次，将行记录作为变量
    """

    def __init__(self):
        super().__init__()
        self.count = None
        self.dict_result = None

    def init(self, param: json, flow: Flow):
        super(For, self).init(param, flow)
        self.count = 0

    def execute(self):
        super(For, self).execute()

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]
        self.dict_result = df.to_df().to_dict(orient="records")

        if self.count == len(self.dict_result):
            self.count = self.count + 1
            self.set_result(None)
            return

        row = self.dict_result[self.count]
        for k, v in row.items():
            self.flow.param_dict["row.{}".format(k)] = v

        self.count = self.count + 1
        self.set_result(None)

    def set_result(self, df: duckdb.DuckDBPyRelation):
        false_step = self.param.get("false_step", None)
        true_or_false = self.count > len(self.dict_result)

        for node in self.next_nodes:
            # 执行完成，false_step没有
            if true_or_false is True and false_step is None:
                loguru.logger.info(" false_step is None")
                break
            # 未执行完成,执行下一步
            if true_or_false is False and node.name != false_step:
                node.execute()
                node.after_execute()
                break
            # 执行完成,执行完成步骤
            if true_or_false is True and node.name == false_step:
                node.execute()
                node.after_execute()
                break

    def to_json(self):
        super(For, self).to_json()
