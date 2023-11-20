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
        path = getProjectPath() + "/doc/1.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()

    def test_parquet_input(self):
        path = getProjectPath() + "/doc/parquet_input_console.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()

    def test_faker(self):
        path = getProjectPath() + "/doc/faker_input_console.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()

    def test_http_input(self):
        path = getProjectPath() + "/doc/http_input_console.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()
        myFlow.close()


    def test_ckInput(self):
        path = getProjectPath() + "/doc/ck_input_ck_output.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()
        myFlow.close()


    # 自定义插件功能
    def test_Hello(self):
        path = "../doc/hello_input_console.json."
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()
        myFlow.close()

    def test_csvInput_CKOutput(self):
        path = getProjectPath() + "/doc/csv_input_ck_output.json"
        data_dir = "F:\\07_数据源大全\\车站数据\\后两周的数据"
        file_list = os.listdir(data_dir)
        for file in file_list:
            myFlow: Flow = FlowManager.read(path).set_param({"file_name": data_dir + "\\" + file})
            myFlow.run()
            myFlow.close()

    # akshare
    def test_AKShare(self):
        path = getProjectPath() + "/doc/akshare_input_csv_output.json."
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()
        myFlow.close()

    def test_mysql_input(self):
        path = getProjectPath() + "/doc/mysql_input_console.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()
        myFlow.close()

    def test_duckdb_input(self):
        path = getProjectPath() + "/doc/duckdb_input_console.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()
        myFlow.close()


if __name__ == '__main__':
    unittest.main()
