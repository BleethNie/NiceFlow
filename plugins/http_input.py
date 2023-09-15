import json
from sanic import Sanic, text, Config

import duckdb
import pandas as pd

from core.flow import Flow
from core.plugin import IPlugin


class MyConfig(Config):
    PLUGIN:IPlugin = None



class HttpInput(IPlugin):

    app = Sanic('myapp',config=MyConfig())

    @app.post("/data")
    async def hello_world(request):
        app = Sanic.get_app("myapp")
        print(app.config.PLUGIN)
        print(request)
        return text("handler_url")

    def init(self, param: json, flow: Flow):
        super(HttpInput, self).init(param, flow)

    def execute(self):
        # 启动一个server
        port = self.param["port"]
        handler_url = self.param["handler_url"]
        print("启动了一个httpserver,端口号【{}】,处理路径【{}】,请求方式【POST】".format(port, handler_url))
        app = Sanic.get_app("myapp")
        app.config.PLUGIN = "aaa"
        app.run(host="0.0.0.0", port=port)

    def to_json(self):
        super(HttpInput, self).to_json()

    def close(self):
        super(HttpInput, self).close()

    def do_post(self):
        if self.path == self.param["handler_url"]:
            data = self.rfile.read(int(self.headers["content-length"]))
            datas = json.loads(data)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write({"code": 200, "msg": "数据导入成功"})
            df = pd.DataFrame(datas)
            df = duckdb.from_df(df)
            self.set_result(df)
        else:
            print("无效的处理路径...")
