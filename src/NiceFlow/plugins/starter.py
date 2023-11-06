import json

import pandas as pd

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


# 空执行实际没有啥作用
class Starter(IPlugin):

    def init(self, param: json,flow:Flow):
        super(Starter, self).init(param,flow)

    def execute(self):
        super(Starter, self).execute()
        df = pd.DataFrame()
        self.set_result(df)

    def to_json(self):
        super(Starter, self).to_json()
