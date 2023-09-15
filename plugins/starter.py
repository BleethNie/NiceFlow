import json

import duckdb

from core.plugin import IPlugin


class Starter(IPlugin):

    def init(self, param: json):
        super(Starter, self).init(param)

    def execute(self):
        self.param[""]



    def to_json(self):
        super(Starter, self).to_json()
