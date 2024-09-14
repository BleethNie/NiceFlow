import json

import duckdb
from loguru import logger

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


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

        script_str = f'ak.{api_name}({k_v_str})'
        logger.info(f"执行脚本为：{script_str}" )

        # 脚本编译执行
        import akshare as ak
        compile_obj = compile(script_str, '', 'eval')
        df = eval(compile_obj)

        duck_df = duckdb.from_df(df)
        # 写入结果
        self.set_result(duck_df)

    def to_json(self):
        super(AKShareInput, self).to_json()
