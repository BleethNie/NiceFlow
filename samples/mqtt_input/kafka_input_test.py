import unittest

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestKafkaInput(unittest.TestCase):

    def test_kafka_input(self):
        path = "kafka_input_for_console.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()



if __name__ == '__main__':
    unittest.main()
