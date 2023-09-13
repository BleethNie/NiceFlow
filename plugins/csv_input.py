import json

from core.plugin import IPlugin


class CsvInput(IPlugin):

    def init(self, param: json):
        print(param)

    def execute(self):
        print("nice csv-input")
        return 2
