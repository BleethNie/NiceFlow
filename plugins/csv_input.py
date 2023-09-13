import json

from core.plugin import IPlugin


class CsvInput(IPlugin):

    def init(self, param: json):
        super(CsvInput, self).init(param)

    def execute(self):
        print("nice csv-input")
        for node in self.next_nodes:
            node.execute()

    def to_json(self):
        super(CsvInput, self).to_json()
