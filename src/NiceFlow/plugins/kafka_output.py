import json

from kafka import KafkaProducer

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin

from datetime import date, datetime

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)



class KafkaOutput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(KafkaOutput, self).init(param, flow)

    def execute(self):
        super(KafkaOutput, self).execute()
        bootstrap_servers = self.param.get("bootstrap_servers", ["127.0.0.1:9020"])
        topic_name = self.param.get("topic_name")

        producer = KafkaProducer(bootstrap_servers=bootstrap_servers,key_serializer=lambda k: json.dumps(k).encode(),      # 假设生产的消息为json字符串
                                 value_serializer=lambda v: json.dumps(v, cls=ComplexEncoder).encode())

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]

        num = 1
        while True:
            list = df.fetchmany(1000)
            print(f"num = {num} list size = {len(list)}")
            num = num + 1
            if list is None or len(list) == 0:
                break
            for row in list:
                data = dict(zip(df.columns, row))
                producer.send(topic_name,data)

    def to_json(self):
        super(KafkaOutput, self).to_json()

    def close(self):
        super(KafkaOutput, self).close()
