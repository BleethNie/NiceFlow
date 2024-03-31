import json

import duckdb
import pandas as pd

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin
import paho.mqtt.client as mqtt


class MqttInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(MqttInput, self).init(param, flow)

    def on_connect(self, client, userdata, flags, rc):
        # 0: Connection successful
        # 1: Connection refused - incorrect protocol version
        # 2: Connection refused - invalid client identifier
        # 3: Connection refused - server unavailable
        # 4: Connection refused - bad username or password
        # 5: Connection refused - not authorised
        # 6-255: Currently unused.
        if rc == 0:
            print("Connection successful")
        if rc == 1:
            print("Connection refused - incorrect protocol version")
        if rc == 2:
            print("Connection refused - invalid client identifier")
        if rc == 3:
            print("Connection refused - server unavailable")
        if rc == 4:
            print("Connection refused - bad username or password")
        if rc == 5:
            print("Connection refused - not authorised")
        if rc!=0:
            return
        # 在连接建立后订阅主题
        client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        msg_str = msg.payload.decode('utf-8')
        json_data = json.loads(msg_str)
        if isinstance(json_data,list):
            df = pd.DataFrame(json_data)
        else:
            df = pd.DataFrame([json_data])
        ck_df = duckdb.from_df(df)
        # 写入结果
        self.set_result(ck_df)

    def execute(self):
        super(MqttInput, self).execute()

        # param信息
        host = self.param["host"]
        port = self.param.get("port", 1883)
        self.topic = self.param.get("topic", "")
        username = self.param.get("username", None)
        password = self.param.get("password", None)
        clientId = self.param.get("client_id", "")

        # 配置数据库
        if clientId:
            client = mqtt.Client(client_id=clientId)
        else:
            client = mqtt.Client()

        # 配置消息回调
        client.on_connect = self.on_connect
        client.on_message = self.on_message

        if username:
            client.username_pw_set(username=username, password=password)

        client.connect(host, port)
        client.loop_forever()

    def to_json(self):
        super(MqttInput, self).to_json()
