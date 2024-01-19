import unittest

import sqlglot

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestDuckDBInput(unittest.TestCase):


    def test_import_data_to_mysql(self):
        path = "duckdb_input_from_mysql_to_parquet.json"
        myFlow: Flow = FlowManager.read(path)
        flow_param = {
            "path": "",
            "sql": '''
             LOAD mysql;

             ATTACH 'host=localhost user=root password=123456 port=3306 database=che' AS mysqldb (TYPE mysql);
             ATTACH ':memory:' AS db1;
            CREATE TABLE db1.che_test AS SELECT * FROM read_csv_auto('F:/07_数据源大全/车站数据/后两周的数据/bus0416.csv');
            CREATE TABLE mysqldb.che_test AS SELECT * FROM  db1.che_test;
            ''',
        }
        # 导入8480496行数据，执行完成需要4分46秒
        myFlow.set_param(flow_param)
        myFlow.run()



    def test_export_mysql_data(self):
        path = "duckdb_input_from_mysql_to_parquet.json"
        myFlow: Flow = FlowManager.read(path)
        flow_param = {
            "path": "",
            "sql": '''
             LOAD mysql;
             ATTACH 'host=localhost user=root password=123456 port=3306 database=che' AS mysqldb (TYPE mysql);
             USE mysqldb;

             COPY (SELECT * FROM che_test ) TO 'che_test_1.parquet';
            ''',
        }
        # 从mysql导出8480496行数据，执行完成需要20秒
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
              CREATE TABLE che_test AS SELECT * FROM read_parquet('che_test_1.parquet');
              -- CREATE TABLE che_test AS SELECT * FROM read_csv_auto('F:/07_数据源大全/车站数据/后两周的数据/bus0416.csv');
              -- select count(*) from che_test where up_time>='2018-01-16 10:44:01' and grant_card_code='38480150';
              {duck_query}
            ''',
        }
        myFlow.set_param(flow_param)
        myFlow.run()
        result_dict = myFlow.get_result()
        duck_df = list(result_dict.values())[0]
        print(duck_df)




if __name__ == '__main__':
    unittest.main()
