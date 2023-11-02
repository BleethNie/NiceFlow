import json

from confluent_kafka import Consumer

from core.flow import Flow
from core.plugin import IPlugin


class KafkaOutput(IPlugin):

        def init(self, param: json, flow: Flow):
                super(KafkaOutput, self).init(param, flow)

        def execute(self):
                conf = {'bootstrap.servers': 'host1:9092,host2:9092',
                        'group.id': 'foo',
                        'auto.offset.reset': 'smallest'}

                consumer = Consumer(conf)


        def to_json(self):
                super(KafkaOutput, self).to_json()

        def close(self):
                super(KafkaOutput, self).close()
