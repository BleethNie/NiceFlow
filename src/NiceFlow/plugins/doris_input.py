import json

import pandas
from sqlalchemy import create_engine
from sqlalchemy.sql.expression import text

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class DorisInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(DorisInput, self).init(param,flow)

    def execute(self):
        super(DorisInput, self).execute()
        engine = create_engine('doris://root:xxx@localhost:9030/hive_catalog.hive_db')
        connection = engine.connect()
        rows = connection.execute(text("SELECT * FROM hive_table")).fetchall()
        df = pandas.DataFrame(rows)
        # 设置下一步结果
        self.set_result(df)

    def to_json(self):
        super(DorisInput, self).to_json()
