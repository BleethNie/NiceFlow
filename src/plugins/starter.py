import json

import pandas as pd

from src.core.flow import Flow
from src.core.plugin import IPlugin


# 空执行实际没有啥作用
class Starter(IPlugin):

    def init(self, param: json,flow:Flow):
        super(Starter, self).init(param,flow)

    def execute(self):
        df = pd.DataFrame()
        self.set_result(df)

    def to_json(self):
        super(Starter, self).to_json()
