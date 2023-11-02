import json

from confluent_kafka import Consumer

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class PaimonOutput(IPlugin):

        def init(self, param: json, flow: Flow):
                super(PaimonOutput, self).init(param, flow)

        def execute(self):
                conf = {'bootstrap.servers': 'host1:9092,host2:9092',
                        'group.id': 'foo',
                        'auto.offset.reset': 'smallest'}

                consumer = Consumer(conf)


        def to_json(self):
                super(PaimonOutput, self).to_json()

        def close(self):
                super(PaimonOutput, self).close()
