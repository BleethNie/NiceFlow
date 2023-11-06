import json

import duckdb
from loguru import logger
import pandas as pd
from clickhouse_driver import Client

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin
import akshare as ak


class AKShareInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(AKShareInput, self).init(param, flow)

    def execute(self):
        super(AKShareInput, self).execute()
        # param信息
        api_name = self.param["api_name"]
        params = self.param.get("params", {})
        k_v_str = None
        for key, value in params.items():
            if k_v_str is None:
                k_v_str = ""
            k_v_str = k_v_str + "{}='{}',".format(key, value)
        k_v_str = k_v_str.removesuffix(",")
        script_str = "ak.{api_name}({k_v})".format(api_name=api_name, k_v=k_v_str)
        logger.info("执行脚本为：{}", script_str)
        compile_obj = compile(script_str, '', 'eval')
        df = eval(compile_obj)
        duck_df = duckdb.from_df(df)
        # 写入结果
        self.set_result(duck_df)

    def to_json(self):
        super(AKShareInput, self).to_json()
