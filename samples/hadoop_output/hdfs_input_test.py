import unittest

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestDuckDBInput(unittest.TestCase):


    def test_import_data_to_mysql(self):
        path = "duckdb_input_to_hdfs.json"
        myFlow: Flow = FlowManager.read(path)
        flow_param ={}
        myFlow.set_param(flow_param)
        myFlow.run()


if __name__ == '__main__':
    unittest.main()
