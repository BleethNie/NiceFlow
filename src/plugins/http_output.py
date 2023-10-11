import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from src.core.flow import Flow
from src.core.plugin import IPlugin


class HttpOutput(IPlugin):

    def init(self, param: json, flow: Flow):
        super().init(param, flow)

    def make_handler(plugin: IPlugin):
        class ResultHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                # 解析URL中的查询字符串
                query = parse_qs(urlparse(self.path).query)

                # 获取参数值
                orient = query.get('orient', "values")[0]

                pre_node = plugin.pre_nodes[0]
                df = plugin._pre_result_dict[pre_node.name]

                self.send_response(200)
                # 发给请求客户端的响应数据
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                data = json.loads(df.to_df().to_json(orient = orient))
                self.wfile.write(json.dumps({"data":data }).encode())

        return ResultHandler

    def execute(self):
        # 启动一个server
        host = self.param.get("host", "0.0.0.0")
        port = self.param["port"]
        handler_url = self.param.get("handler_url","")
        host_info = (host, port)
        server = HTTPServer(host_info, self.make_handler())
        print("host启动成功，http://{}:{}".format(host_info[0], host_info[1]))
        server.serve_forever()  # 开启服务

    def to_json(self):
        super().to_json()

    def close(self):
        super().close()
