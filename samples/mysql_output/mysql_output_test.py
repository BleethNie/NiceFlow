import unittest

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestMysqlOutput(unittest.TestCase):

    def test_insert(self):
        path = "mysql_input_for_mysql_output_insert.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()
    def test_merge(self):
        path = "mysql_input_for_mysql_output_merge.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()


if __name__ == '__main__':
    unittest.main()
