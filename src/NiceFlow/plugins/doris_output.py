import uuid

from pydoris.doris_client import *

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class DorisOutput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(DorisOutput, self).init(param, flow)

    def execute(self):
        super(DorisOutput, self).execute()
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        my_df = self._pre_result_dict[pre_node.name]

        fe_host = self.param.get("fe_host", "127.0.0.1")
        fe_http_port = self.param.get("fe_http_port", "8040")
        db = self.param.get("db", "")
        table = self.param.get("table", "")
        username = self.param.get("username", "root")
        password = self.param.get("password", "123456")
        #
        # doris_client = DorisClient(fe_host=fe_host,
        #                            fe_query_port=fe_query_port,
        #                            fe_http_port=fe_http_port,
        #                            username=username,
        #                            password=password,
        #                            db=db)
        # doris_client.write_from_df(my_df.to_df(), f"{db}.{table}", "unique", ['id'], )
        my_df.to_parquet("a.parquet")
        upload_file(fe_host, fe_http_port, db, table, "a.parquet", username, password, "1111")

        self.set_result(None)

    def to_json(self):
        super(DorisOutput, self).to_json()


def upload_file(fe_host: str, fe_http_port: str, db: str, table: str, filepath: str, username: str, password: str):
    url = f'http://{fe_host}:{fe_http_port}/api/{db}/{table}/_stream_load'
    doris_headers = {
        'label': str(uuid.uuid1()),
        'column_separator': ';',
        'expect': '100 continue',
        "format": "parquet",
        'Content-Type': 'application/octet-stream'
    }
    auth = HTTPBasicAuth(username, password)
    p_file = open(filepath, "rb")
    file = {'file': p_file}
    response = requests.put(url, data=None, files=file, headers=doris_headers, auth=auth)
    print(response.text)
    p_file.close()
