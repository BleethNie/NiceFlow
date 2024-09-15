import unittest

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestSQL(unittest.TestCase):

    def test_sql(self):
        path = "csv_excel_input_sql_console.json"
        myFlow: Flow = FlowManager.read(path)
        flow_param = {
        }
        myFlow.set_param(flow_param)
        myFlow.run()




if __name__ == '__main__':
    unittest.main()
