import json

import duckdb
from odps import ODPS

from core.flow import Flow
from core.plugin import IPlugin


class ODPSInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super().init(param, flow)

    def execute(self):
        # param信息
        access_key = self.param["access_key"]
        access_secret = self.param.get("access_secret", "")
        project = self.param.get("project", "")
        end_point = self.param.get("end_point", "")
        sql = self.param["sql"]

        o = ODPS(access_key, access_secret,
                 project=project, endpoint=end_point)
        query_job = o.execute_sql(sql)
        result = query_job.open_reader(tunnel=True)
        df = result.to_pandas(n_process=1)  # n_process配置可参考机器配置，取值大于1时可以开启多线程加速。
        odps_df = duckdb.from_df(df)
        # 写入结果
        self.set_result(odps_df)


    def to_json(self):
        super().to_json()

    def close(self):
        super().close()
