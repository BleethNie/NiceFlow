import json

from core.plugin import IPlugin


class CsvInput(IPlugin):

    def init(self, param: json):
        super(CsvInput, self).init(param)

    def execute(self):
        print("nice csv-input")
        return 2

    def to_json(self):
        return {
            "name": self.name,
            "id": self.id,
            "type": self.type,
            "properties": self.param
        }
