import unittest

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestExcelInput(unittest.TestCase):

    def test_excel_input(self):
        path = "excel_input_to_console.json"
        myFlow: Flow = FlowManager.read(path)
        flow_param = {
            "filename": "total_RQ_SITE_20231226.xlsx",
        }
        myFlow.set_param(flow_param)
        myFlow.run()

        # 从执行中获取结果
        result_dict = myFlow.get_result()
        duck_df = list(result_dict.values())[0]
        print(duck_df)


if __name__ == '__main__':
    unittest.main()
