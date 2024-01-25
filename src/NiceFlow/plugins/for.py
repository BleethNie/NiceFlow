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
        self.count = 1

    def receiver(self, sender):
        self.execute()

    def execute(self):
        super(For, self).execute()

        # TODO:获取上一步结果 不能是final_step
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]
        self.dict_result = df.to_df().to_dict(orient="records")

        if self.count == len(self.dict_result)+2:
            loguru.logger.debug("self.count == len(self.dict_result)+2")
            # 执行结束
            return

        if self.count == len(self.dict_result)+1:
            loguru.logger.debug("执行set_result  len(self.dict_result)+1")
            # 执行结束
            self.set_result(df)
            return

        row = self.dict_result[self.count-1]
        for k, v in row.items():
            self.flow.param_dict["row.{}".format(k)] = v


        self.set_result(df)


    def set_result(self, df: duckdb.DuckDBPyRelation):
            loguru.logger.debug("执行set_result")
            finish_step = self.param.get("finish_step", None)

            # 设置结果
            for node in self.next_nodes:
                node._pre_result_dict[self.name] = df

            true_or_false = self.count > len(self.dict_result)
            self.count = self.count + 1


            if true_or_false is True:
                if finish_step is not None :
                    loguru.logger.info("执行完成,执行完成步骤")
                    self.flow.plugin_dict[finish_step].execute()
                    self.count = 1
                    return

            if true_or_false is False:
                for node in self.next_nodes:
                    if finish_step is not None and node.name ==  finish_step:
                        continue
                    node.execute()

    def to_json(self):
        super(For, self).to_json()
