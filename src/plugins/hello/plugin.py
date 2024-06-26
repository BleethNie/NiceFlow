import json

import duckdb
import pandas as pd

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class HelloInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(HelloInput, self).init(param, flow)

    def execute(self):
        super(HelloInput, self).execute()
        df = pd.DataFrame([{"F1":"1","F2":"2"}])
        duck_df = duckdb.from_df(df)
        # 写入结果
        self.set_result(duck_df)


    def to_json(self):
        super(HelloInput, self).to_json()
