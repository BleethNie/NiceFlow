import json

import duckdb
import pandas as pd

from core.flow import Flow
from core.plugin import IPlugin


class HelloInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(HelloInput, self).init(param, flow)

    def execute(self):
       df = pd.DataFrame([{"F1":"1","F2":"2"}])
       ck_df = duckdb.from_df(df)
       # 写入结果
       self.set_result(ck_df)


    def to_json(self):
        super(HelloInput, self).to_json()
