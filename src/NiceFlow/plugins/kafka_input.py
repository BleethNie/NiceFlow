import json
import threading

from kafka import KafkaConsumer

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class KafkaInput(IPlugin):

    def stop(self):
        self.stop_event.set()

    def init(self, param: json, flow: Flow):
        super(KafkaInput, self).init(param, flow)
        self.stop_event = threading.Event()

    def execute(self):
        super(KafkaInput, self).execute()

        # param信息
        hosts = self.param.get("hosts", [])
        topic = self.param.get("topic", "")

        consumer = KafkaConsumer(bootstrap_servers=hosts,
                                 auto_offset_reset='earliest',
                                 consumer_timeout_ms=1000)
        # 订阅要消费的主题
        consumer.subscribe(topics=[topic])
        while not self.stop_event.is_set():
            for message in consumer:
                print(message)
                if self.stop_event.is_set():
                    break

        consumer.close()

        # while True:
        #     msg = consumer.poll()
        #     json_data = json.loads(msg)
        #     if isinstance(json_data,list):
        #         df = pd.DataFrame(json_data)
        #     else:
        #         df = pd.DataFrame([json_data])
        #     ck_df = duckdb.from_df(df)
        #     # 写入结果
        #     self.set_result(ck_df)

    def to_json(self):
        super(KafkaInput, self).to_json()
