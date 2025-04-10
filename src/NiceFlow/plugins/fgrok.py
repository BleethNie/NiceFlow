import json

import duckdb

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin
from loguru import logger
from pygrok import Grok


def function_grok(col: str, pattern: str) -> str:
    grok = Grok(pattern)
    res = grok.match(col)
    return res


class FGrok(IPlugin):

    def init(self, param: json, flow: Flow):
        super(FGrok, self).init(param, flow)
        duckdb.create_function('function_grok', function_grok)

    def execute(self):
        super(FGrok, self).execute()
        pattern = self.param["pattern"]
        field = self.param["field"]

        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        df = self._pre_result_dict[pre_node.name]

        sql = "select *,function_grok( {} ,'{}') as {}_grok from df" \
            .format(field, pattern, field)
        logger.info(f"执行sql = {sql}")
        df = duckdb.from_df(duckdb.sql(sql).df())
        self.set_result(df)

    def to_json(self):
        super(FGrok, self).to_json()

    def close(self):
        super(FGrok, self).close()
        duckdb.remove_function("function_grok")


if __name__ == '__main__':
    pattern = "%{TIMESTAMP_ISO8601:date},%{NUMBER:date_s}%{SPACE}"
    msg = "2025-04-10 21:04:04,250 [Quartz Scheduler [clusterScheduler]] INFO  o.s.s.quartz.SchedulerFactoryBean ? - Starting Quartz Scheduler now, after delay of 60 seconds"
    grok = Grok(pattern)
    res = grok.match(msg)
    print(res)
