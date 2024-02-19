import unittest

import sqlglot

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestESInput(unittest.TestCase):

    def test_es_input_to_console(self):
        path = "duckdb_input_from_mysql_to_parquet.json"
        myFlow: Flow = FlowManager.read(path)
        flow_param = {
            "url": "",
            "index": "",
            "query": ""
        }
        myFlow.set_param(flow_param)
        myFlow.run()


if __name__ == '__main__':
    unittest.main()
