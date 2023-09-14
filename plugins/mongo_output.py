import json

from pymongo import MongoClient

from core.plugin import IPlugin


class MongoOutput(IPlugin):

    def __init__(self):
        super().__init__()

    def init(self, param: json):
        super(MongoOutput, self).init(param)
        self.client = MongoClient("uri")

    def execute(self):
        db = self.client['database_name']
        collection = db['collection_name']

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]

        # 写入mongo
        data_dictionary = df.to_dict()
        collection.insert_many(data_dictionary)


    def to_json(self):
        super(MongoOutput, self).to_json()
