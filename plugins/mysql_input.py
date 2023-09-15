import json

import pandas
from sqlalchemy import create_engine
from sqlalchemy.sql.expression import text

from core.plugin import IPlugin


class MySQLInput(IPlugin):

    def init(self, param: json):
        super(MySQLInput, self).init(param)

    def execute(self):
        engine = create_engine('doris://root:xxx@localhost:9030/hive_catalog.hive_db')
        connection = engine.connect()
        rows = connection.execute(text("SELECT * FROM hive_table")).fetchall()
        df = pandas.DataFrame(rows)
        # 设置下一步结果
        self.set_result(df)

    def to_json(self):
        super(MySQLInput, self).to_json()
