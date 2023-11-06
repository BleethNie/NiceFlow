import unittest

import duckdb

data_dir = "C:/Users/xiaow/Desktop/差额排查"


class TestDuckDB(unittest.TestCase):

    def test_base(self):
        total_df = duckdb.read_csv(data_dir + "/87市场销售额.txt")
        self_df = duckdb.read_csv(data_dir + "/87自己的销售额.txt")
        other_df = duckdb.read_csv(data_dir + "/other市场销售额.txt")
        final_df = duckdb.sql('''
                select total_df.*,self_df.self_sale_amount,other_df.other_total_sale_amount
                from total_df 
                left join self_df on total_df.date_day = self_df.date_day
                left join other_df on total_df.date_day = other_df.date_day
                order by total_df.date_day desc
                ''')
        final_df.to_df().to_excel(data_dir + "/result.xlsx", index=False)


if __name__ == '__main__':
    unittest.main()
