import os
import unittest

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager
from NiceFlow.core.mysqldb_logging_handler import MySQLDBLogHandler


def getProjectPath() -> str:
    # 获取当前文件的绝对路径
    current_file = os.path.abspath(__file__)
    # 获取当前文件所在目录的绝对路径
    current_directory = os.path.dirname(current_file)
    # 获取当前项目的根目录
    project_root = os.path.dirname(os.path.dirname(current_directory))
    return project_root


class TestFlow(unittest.TestCase):

    def test_param(self):
        path = "E:/02_Resource/01_Code/python/NiceFlow/doc/flow/flow_param_console.json"
        myFlow: Flow = FlowManager.read(path)
        flow_param = {
            "file_name": "F:/07_数据源大全/store_order/channel.csv",
            "row": 20
        }
        myFlow.set_param(flow_param)
        myFlow.run()

    def test_mysql_log_handler(self):
        handler = MySQLDBLogHandler()
        Flow.register_log_handler(handler)
        path = getProjectPath() + "/doc/faker_input_console.json"
        myFlow: Flow = FlowManager.read(path)

        myFlow.run()


if __name__ == '__main__':
    unittest.main()
