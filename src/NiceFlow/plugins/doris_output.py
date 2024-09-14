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
        fe_query_port = self.param.get("fe_query_port", "9030")
        db = self.param.get("db", "")
        table = self.param.get("table", "")
        username = self.param.get("username", "root")
        password = self.param.get("password", "123456")


        from pydoris.doris_client import DorisClient

        client = DorisClient(fe_host, fe_query_port,fe_http_port, username, password,db)
        table_path = f"table_{str(uuid.uuid1())}.parquet"
        my_df.to_df().to_parquet(table_path,engine="pyarrow",index=False)
        b = open(table_path, 'rb')
        option = WriteOptions()
        option.set_auto_uuid_label()\
            .set_format("parquet")\
            .set_option("column_separator",",")\
            .set_option("columns","")\
        .set_option("max_filter_ratio","20")
        client.write(table_name="test.news_record",data=b,options=option)


        # doris_helper=make_doris_helper(fe_host, fe_http_port, username, password)


        # doris_helper.upload_csv(db, table, table_path)

        self.set_result(None)

    def to_json(self):
        super(DorisOutput, self).to_json()


class DorisHelper():
    def __init__(self, fe_host: str, fe_http_port: str, username: str, password: str):
        self.fe_host = fe_host
        self.fe_http_port = fe_http_port
        self.username = username
        self.password = password

    def upload_parquet(self, db: str, table: str, filepath: str):
        doris_headers = {
            'label': str(uuid.uuid1()),
            'column_separator': ';',
            "format": "parquet",
            'Content-Type': 'application/octet-stream'
        }
        stream_file = open(filepath, "rb")
        self._upload(db, table, doris_headers, stream_file)



    def upload_json(self, db: str, table: str, filepath: str):
        doris_headers = {
            'label': str(uuid.uuid1()),
            'column_separator': ';',
            "format": "json",
            'Content-Type': 'application/octet-stream'
        }
        stream_file = open(filepath, "rb")
        self._upload(db, table, doris_headers, stream_file)



    def upload_orc(self, db: str, table: str, filepath: str):
        doris_headers = {
            'label': str(uuid.uuid1()),
            'column_separator': ';',
            "format": "orc",
            'Content-Type': 'application/octet-stream'
        }
        stream_file = open(filepath, "rb")
        self._upload(db, table, doris_headers, stream_file)


    def upload_csv(self, db: str, table: str, filepath: str):
        doris_headers = {
            'label': str(uuid.uuid1()),
            'column_separator': ';',
            "format": "csv",
            'Content-Type': 'application/octet-stream'
        }
        stream_file = open(filepath, "rb")
        self._upload(db, table, doris_headers, stream_file)


    def _upload(self, db: str, table: str, headers, stream_file):
        url = f'http://{self.fe_host}:{self.fe_http_port}/api/{db}/{table}/_stream_load'
        auth = HTTPBasicAuth(self.username, self.password)
        file = {'file': stream_file}
        response = requests.put(url, data=None, files=file, headers=headers, auth=auth)
        print(response.text)
        stream_file.close()


def make_doris_helper(fe_host: str, fe_http_port: str, username: str, password: str):
    return DorisHelper(fe_host, fe_http_port, username, password)
