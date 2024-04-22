import unittest


from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestESOutput(unittest.TestCase):

    def test_faker_to_es_output(self):
        path = "es_output_to_console.json"
        myFlow: Flow = FlowManager.read(path)
        flow_param = {
            "url": "http://127.0.0.1:9200",
            "index": "test"
        }
        myFlow.set_param(flow_param)
        myFlow.run()


if __name__ == '__main__':
    unittest.main()
