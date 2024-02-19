import unittest

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestDuckDBInput(unittest.TestCase):


    def test_import_data_to_mysql(self):
        path = "mysql_input_to_hdfs.json"
        myFlow: Flow = FlowManager.read(path)
        flow_param ={}
        myFlow.set_param(flow_param)
        myFlow.run()

    def test_http(self):
        path = "http_for_mysql_hdfs.json"
        myFlow: Flow = FlowManager.read(path)
        flow_param ={}
        myFlow.set_param(flow_param)
        myFlow.run()

    def test_hdfs_import_data_to_mysql(self):
        path = "mysql_input_to_hdfs_all_sync.json"
        myFlow: Flow = FlowManager.read(path)
        flow_param ={}
        myFlow.set_param(flow_param)
        myFlow.run()


if __name__ == '__main__':
    unittest.main()
