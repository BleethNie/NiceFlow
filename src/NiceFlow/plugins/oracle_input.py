import json

import duckdb
from odps import ODPS

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class OracleInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(OracleInput, self).init(param, flow)

    def execute(self):
        super(OracleInput, self).execute()

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
        df = result.to_pandas(n_process=1)
        odps_df = duckdb.from_df(df)
        # 写入结果
        self.set_result(odps_df)


    def to_json(self):
        super(OracleInput, self).to_json()

    def close(self):
        super(OracleInput, self).close()
