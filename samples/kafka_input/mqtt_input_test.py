import unittest

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestMqttInput(unittest.TestCase):

    def test_mqtt_input(self):
        path = "mqtt_input_for_mysql_output.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()



if __name__ == '__main__':
    unittest.main()
