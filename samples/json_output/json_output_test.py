import unittest


from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestJsonOutput(unittest.TestCase):

    def test_Json_output(self):
        path = "faker_input_json_output.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()


if __name__ == '__main__':
    unittest.main()
