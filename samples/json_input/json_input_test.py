import unittest

import duckdb.duckdb

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestJsonInput(unittest.TestCase):

    def test_Json_input(self):
        path = "json_input_for_console.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()

    def test_Json_input_mysql_output(self):
        path = "json_input_for_doris_out.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()

    def test_parquet_input_doris_output(self):
        path = "parquet_input_for_doris_out.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()

    def test_read_parquet(self):
        file_name  ="table_38879b32-6e73-11ef-a882-581cf802095d.parquet"
        df = duckdb.read_parquet(file_name)
        print(len(df))
        df.show()



if __name__ == '__main__':
    unittest.main()
