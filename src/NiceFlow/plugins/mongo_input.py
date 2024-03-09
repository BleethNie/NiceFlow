import json

import duckdb
import pandas as pd
from pymongo import MongoClient

from NiceFlow.core.plugin import IPlugin


class MongoInput(IPlugin):

    def __init__(self):
        super().__init__()

    def init(self, param: json):
        super(MongoInput, self).init(param)
        self.client = MongoClient("uri")

    def execute(self):
        super(MongoInput, self).execute()

        db = self.client['database_name']
        collection = db['collection_name']
        df = pd.DataFrame(list(collection.find()))
        duck_df = duckdb.from_df(df)
        self.set_result(duck_df)

    def to_json(self):
        super(MongoInput, self).to_json()
