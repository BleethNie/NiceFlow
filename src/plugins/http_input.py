import json
from http.server import HTTPServer, BaseHTTPRequestHandler

import duckdb
import pandas as pd

from src.core.flow import Flow
from src.core.plugin import IPlugin


class HttpInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super().init(param, flow)

    def make_handler(plugin: IPlugin):
        class ResultHandler(BaseHTTPRequestHandler):
            def do_POST(self):
                content_length = int(self.headers.get('Content-Length'))
                post_body_byte = self.rfile.read(content_length)
                post_body = str(post_body_byte, 'utf-8')
                df = pd.read_json(post_body)
                df = duckdb.from_df(df)
                plugin.set_result(df)

                self.send_response(200)
                # 发给请求客户端的响应数据
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"msg": "读取成功"}).encode())

        return ResultHandler

    def execute(self):
        # 启动一个server
        host = self.param.get("host", "0.0.0.0")
        port = self.param["port"]
        handler_url = self.param["handler_url"]
        host_info = (host, port)
        server = HTTPServer(host_info, self.make_handler())
        print("host启动成功，http://{}:{}".format(host_info[0], host_info[1]))
        server.serve_forever()  # 开启服务

    def to_json(self):
        super().to_json()

    def close(self):
        super().close()
