import json

import duckdb
from loguru import logger

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class While(IPlugin):

    def init(self, param: json,flow:Flow):
        super(While, self).init(param,flow)

    def execute(self):
        super(While, self).execute()
        self.set_result(None)

    def set_result(self, df: duckdb.DuckDBPyRelation):
        decide_script = self.param["decide"]
        false_step = self.param.get("false_step",None)
        logger.info(decide_script)
        compile_obj = compile(decide_script, '', 'eval')
        true_or_false = eval(compile_obj)

        for node in self.next_nodes:
            # 执行完成，false_step没有
            if true_or_false is False and false_step is None:
                logger.info(" false_step is None")
                break
            # 未执行完成,执行下一步
            if true_or_false and node.name != false_step:
                node.before_execute()
                node.execute()
                node.after_execute()
                break
            # 执行完成,执行完成步骤
            if true_or_false is False and node.name == false_step:
                node.before_execute()
                node.execute()
                node.after_execute()
                break


    def to_json(self):
        super(While, self).to_json()
