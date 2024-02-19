import json

import duckdb
import pandas as pd
from elasticsearch import Elasticsearch

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class ESInput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(ESInput, self).init(param, flow)

    def execute(self):
        super(ESInput, self).execute()
        # param信息
        url = self.param["url"]
        index = self.param.get("index", "")
        query = self.param.get("query", "")

        # 配置数据库
        es = Elasticsearch(hosts=url)
        res = es.search(index=index, scroll='1m', body=query)
        sid = res['_scroll_id']
        scroll_size_max = res['hits']['total']['value']
        count = 0
        print(scroll_size_max)

        save_data = []
        while count < scroll_size_max:
            for data in res['hits']['hits']:
                print(count, data)
                save_data.append(data['_source'])
                count += 1
            res = es.scroll(scroll_id=sid, scroll='2m')
            sid = res['_scroll_id']

        # 清除scroll_id
        es.clear_scroll(scroll_id=sid)
        df = pd.DataFrame(save_data)
        duck_df = duckdb.from_df(df)
        # 写入结果
        self.set_result(duck_df)

    def to_json(self):
        super(ESInput, self).to_json()
