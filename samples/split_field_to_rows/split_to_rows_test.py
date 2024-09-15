import unittest

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestSplitToRows(unittest.TestCase):

    def test_split_to_rows(self):
        path = "split_to_rows_for_console.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()

if __name__ == '__main__':
    unittest.main()
