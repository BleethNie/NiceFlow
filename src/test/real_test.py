import os
import unittest

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


def getProjectPath() -> str:
    # 获取当前文件的绝对路径
    current_file = os.path.abspath(__file__)
    # 获取当前文件所在目录的绝对路径
    current_directory = os.path.dirname(current_file)
    # 获取当前项目的根目录
    project_root = os.path.dirname(os.path.dirname(current_directory))
    return project_root


class TestInputPlugin(unittest.TestCase):

    def test_base(self):
        path = getProjectPath() + "/doc/real/监测点.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()

    def test_base_1(self):
        path = getProjectPath() + "/doc/real/设备.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()

if __name__ == '__main__':
    unittest.main()
