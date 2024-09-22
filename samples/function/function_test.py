import unittest


from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestFunction(unittest.TestCase):

    def test_function(self):
        path = "faker_input_function.json"
        myFlow: Flow = FlowManager.read(path)
        flow_param = {

        }
        myFlow.set_param(flow_param)
        myFlow.run()


if __name__ == '__main__':
    unittest.main()