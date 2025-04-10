import unittest

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestGrok(unittest.TestCase):

    def test_grok(self):
        path = "console_grok.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()


if __name__ == '__main__':
    unittest.main()