import unittest

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestFunction(unittest.TestCase):

    def test_function(self):
        path = "csv_input_function_console.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()

    def test_function_2(self):
        path = "csv_input_function_console_2.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()



if __name__ == '__main__':
    unittest.main()
