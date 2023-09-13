from core.plugin import IPlugin


class CsvInput(IPlugin):

    def execute(self):
        print("nice csv-input")
        return 2
