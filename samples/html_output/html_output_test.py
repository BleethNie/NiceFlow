import unittest


from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestHtmlOutput(unittest.TestCase):

    def test_html_output(self):
        path = "faker_to_html_output.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()


if __name__ == '__main__':
    unittest.main()
