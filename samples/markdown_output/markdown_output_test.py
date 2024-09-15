import unittest


from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestMarkdownOutput(unittest.TestCase):

    def test_Markdown_Output(self):
        path = "faker_input_markdown.json"
        myFlow: Flow = FlowManager.read(path)
        flow_param = {

        }
        myFlow.set_param(flow_param)
        myFlow.run()




if __name__ == '__main__':
    unittest.main()
