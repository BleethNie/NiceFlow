import unittest

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestAkshareInput(unittest.TestCase):

    def test_akshare_input(self):
        path = "akshare_input_csv_output.json"
        myFlow: Flow = FlowManager.read(path)
        flow_param = {
        }
        myFlow.set_param(flow_param)
        myFlow.run()


if __name__ == '__main__':
    unittest.main()
