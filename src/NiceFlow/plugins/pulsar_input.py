import json

import duckdb
import pandas as pd

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin
import paho.mqtt.client as mqtt


class PulsarInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(PulsarInput, self).init(param, flow)

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("$SYS/#")

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))
        df = pd.DataFrame(msg.payload)
        ck_df = duckdb.from_df(df)
        # 写入结果
        self.set_result(ck_df)


    def execute(self):
        super(PulsarInput, self).execute()

        # param信息
        host = self.param["host"]
        port = self.param.get("port", 1883)

        # 配置数据库
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect(host, port)
        client.loop_forever()

    def to_json(self):
        super(PulsarInput, self).to_json()
