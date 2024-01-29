import json

import duckdb
import pandas as pd

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin
import paho.mqtt.client as mqtt
from paho.mqtt import client as mqtt_client


class MqttInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(MqttInput, self).init(param, flow)

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe("$SYS/#")

    def subscribe(self,client: mqtt_client):
        def on_message(client, userdata, msg):
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            print(msg.topic + " " + str(msg.payload))
            df = pd.DataFrame(msg.payload)
            ck_df = duckdb.from_df(df)
            # 写入结果
            self.set_result(ck_df)

        client.subscribe(self.topic)
        client.on_message = on_message

    def execute(self):
        super(MqttInput, self).execute()

        # param信息
        host = self.param["host"]
        port = self.param.get("port", 1883)
        self.topic = self.param.get("topic", "")
        clientId = self.param.get("client_id", "")

        # 配置数据库
        if clientId:
            client = mqtt.Client(client_id=clientId)
        else:
            client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect(host, port)
        client.loop_forever()

    def to_json(self):
        super(MqttInput, self).to_json()
