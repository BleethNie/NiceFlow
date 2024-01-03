import unittest

import duckdb

data_dir = "C:/Users/xiaow/Desktop/差额排查"


class TestDuckDB(unittest.TestCase):

    def test_base(self):
        total_df = duckdb.read_csv(data_dir + "/87市场销售额.txt")
        self_df = duckdb.read_csv(data_dir + "/87自己的销售额.txt")
        other_df = duckdb.read_csv(data_dir + "/other市场销售额.txt")
        print(other_df.columns)
        final_df = duckdb.read_csv('''
                select total_df.*,self_df.self_sale_amount,other_df.other_total_sale_amount
                from total_df 
                left join self_df on total_df.date_day = self_df.date_day
                left join other_df on total_df.date_day = other_df.date_day
                order by total_df.date_day desc
                ''')
        final_df.to_df().to_excel(data_dir + "/result.xlsx", index=False)


    def test_httpfs(self):
        duckdb.sql('''INSTALL httpfs;''')
        duckdb.sql('''LOAD httpfs;''')
        duckdb.sql('''SELECT * FROM read_parquet('http://192.168.1.88/chfs/shared/tmp/1.parquet');''')


    def test_httpfs_2(self):
        duckdb.sql('''INSTALL httpfs;''')
        duckdb.sql('''LOAD httpfs;''')
        duckdb.sql(''' CREATE TABLE trek_facts AS SELECT * FROM 'https://raw.githubusercontent.com/Alex-Monahan/example_datasets/main/Star_Trek-Season_1.csv';''')
        result= duckdb.execute('''
        DESCRIBE trek_facts;
        DESCRIBE trek_facts;
        DESCRIBE trek_facts;
        ''')
        print(result.df())

    def test_httpfs_3(self):
        duckdb.sql('''INSTALL httpfs;''')
        duckdb.sql('''LOAD httpfs;''')
        duckdb.sql('''CREATE TABLE trek_facta AS SELECT * FROM  'https://192.168.1.88/chfs/shared/tmp/1.parquet';''')

    def test_multi_sql(self):
        sql_script = """
            CREATE TABLE test (a INTEGER, b VARCHAR);
            
            INSERT INTO test VALUES (1, 'hello'), (2, 'world');
            
            SELECT * FROM test;
        """
        # con = duckdb.connect()
        results = duckdb.execute(sql_script).fetch_df()
        duck_df = duckdb.from_df(results)

    def test_repeat_sql(self):
        sql_script = """
                    CREATE TABLE test (a INTEGER, b VARCHAR);
            
            INSERT INTO test VALUES (1, 'hello'), (2, 'world');
            
            SELECT 
            LPAD(ROW_NUMBER() OVER (ORDER BY b) :: VARCHAR, 5, '0') AS seq,
            seq  as '设施编码',
            * FROM test;
        """
        # con = duckdb.connect()
        results = duckdb.execute(sql_script).fetch_df()
        duck_df = duckdb.from_df(results)
        print(duck_df)

    # 设置字段数据类型
    def test_set_table_field_type(self):
        total_df = duckdb.read_csv(data_dir + "/87市场销售额.txt")
        total_df.to_table("total_df")
        duckdb.execute("ALTER TABLE total_df ALTER leader_customer_code TYPE VARCHAR;")
        duck_df = duckdb.query("select * from total_df;")
        print(duck_df.describe())

if __name__ == '__main__':
    unittest.main()


