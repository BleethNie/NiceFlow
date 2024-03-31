import unittest

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestCsvInput(unittest.TestCase):

    def test_Csv_input(self):
        path = "csv_input_for_console.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()



if __name__ == '__main__':
    unittest.main()
