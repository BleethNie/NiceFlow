import unittest

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


if __name__ == '__main__':
    unittest.main()
