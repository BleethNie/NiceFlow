import unittest

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager, PluginManager


class TestLoadUserPlugin(unittest.TestCase):

    def test_load_user_plugin(self):
        path = "faker_input_to_hello.json"
        PluginManager.register_user_plugin("C://Users//xiaow//Downloads//plugins")
        myFlow: Flow = FlowManager.read(path)
        flow_param = {
        }
        myFlow.set_param(flow_param)
        myFlow.run()


if __name__ == '__main__':
    unittest.main()
