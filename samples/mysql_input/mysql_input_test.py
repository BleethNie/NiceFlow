import unittest

import sqlglot

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestMysqlInput(unittest.TestCase):

    def test_import_data_to_mysql(self):
        path = "mysql_input_to_parquet.json"
        myFlow: Flow = FlowManager.read(path)
        flow_param = {
            "query": 'select * from che.cde_config;',
            "sql": '''
                COPY (SELECT * FROM che_df) TO 'cde_config.csv' ;
            ''',
        }
        # 导入8480496行数据，执行完成需要4分46秒
        myFlow.set_param(flow_param)
        myFlow.run()


    def test_show_export_data(self):
        duck_query = sqlglot.transpile('''
                  SELECT DATE_FORMAT(up_time, '%Y-%m-%d %H') AS hourly_data, COUNT(*) as count FROM che_test GROUP BY hourly_data order by hourly_data desc ;
            ''',read="mysql", write="duckdb")[0]
        print(duck_query)
        path = "duckdb_input_from_mysql_to_parquet.json"
        myFlow: Flow = FlowManager.read(path)
        flow_param = {
            "path": "",
            "sql": f'''
                  SELECT count(*) FROM read_parquet('output.parquet');
                
                ''',
        }
        myFlow.set_param(flow_param)
        myFlow.run()
        result_dict = myFlow.get_result()
        duck_df = list(result_dict.values())[0]
        print(duck_df)


if __name__ == '__main__':
    unittest.main()
