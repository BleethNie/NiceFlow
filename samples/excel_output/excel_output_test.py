import unittest

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestExcelOutput(unittest.TestCase):

    def test_excel_output(self):
        path = "excel_output_to_console.json"
        myFlow: Flow = FlowManager.read(path)
        flow_param = {
            "file_name": "total_RQ_SITE_20231226.xlsx",
            "out_name": "out.xlsx",
        }
        myFlow.set_param(flow_param)
        myFlow.run()


if __name__ == '__main__':
    unittest.main()
