import json

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin
from loguru import  logger

# 只对变量做更新
class Variable(IPlugin):

    def init(self, param: json,flow:Flow):
        super(Variable, self).init(param,flow)

    def execute(self):
        super(Variable, self).execute()
        variable = self.param["variable"]
        script = self.param.get("script")
        compile_obj = compile(script, '', 'eval')
        logger.info("{}--xx--{}".format(variable,self))
        self.flow.param_dict[variable] = eval(compile_obj)
        self.set_result(None)



    def to_json(self):
        super(Variable, self).to_json()
