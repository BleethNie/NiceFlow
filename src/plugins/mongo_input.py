import json

import pandas as pd
from pymongo import MongoClient

from src.core.plugin import IPlugin


class MongoInput(IPlugin):

    def __init__(self):
        super().__init__()

    def init(self, param: json):
        super(MongoInput, self).init(param)
        self.client = MongoClient("uri")

    def execute(self):
        db = self.client['database_name']
        collection = db['collection_name']
        df = pd.DataFrame(list(collection.find()))
        self.set_result(df)

    def to_json(self):
        super(MongoInput, self).to_json()
