import json

from pandas import DataFrame
from elasticsearch import Elasticsearch, helpers

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin
from loguru import logger


class ESOutput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(ESOutput, self).init(param, flow)

    def execute(self):
        super(ESOutput, self).execute()
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        duck_df = self._pre_result_dict[pre_node.name]
        logger.debug(self.param)

        # param信息
        url = self.param["url"]
        index = self.param.get("index", "")
        batch_size = self.param.get("batch_size", 20000)
        basic_auth = self.param.get("basic_auth", None)

        # 配置数据库
        es = Elasticsearch(hosts=url,basic_auth=basic_auth)
        # 批量写数据库
        df = duck_df.to_df()
        list_df = [df[i:i + batch_size] for i in range(0, df.shape[0], batch_size)]
        for i, df_chunk in enumerate(list_df):
            helpers.bulk(es, self.generate_actions(df_chunk, index))

        self.set_result(duck_df)

    def to_json(self):
        super(ESOutput, self).to_json()

    def generate_actions(self,df: DataFrame, index_name: str):
        for _, row in df.iterrows():
            yield {
                "_op_type": "index",
                "_index": index_name,
                "_source": row.to_dict()
            }
