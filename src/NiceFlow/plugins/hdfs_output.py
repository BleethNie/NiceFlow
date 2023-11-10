import json

from confluent_kafka import Consumer

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class HDFSOutput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(HDFSOutput, self).init(param, flow)

    def execute(self):
        super(HDFSOutput, self).execute()

        conf = {'bootstrap.servers': 'host1:9092,host2:9092',
                'group.id': 'foo',
                'auto.offset.reset': 'smallest'}

        consumer = Consumer(conf)

    def to_json(self):
        super(HDFSOutput, self).to_json()

    def close(self):
        super(HDFSOutput, self).close()
