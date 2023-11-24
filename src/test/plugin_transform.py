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


class TestPlugin(unittest.TestCase):

    def test_base(self):
        path = getProjectPath() + "/doc/1.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()

    def test_sort(self):
        path = getProjectPath() + "/doc/sort_console.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()
        myFlow.close()

    def test_samples(self):
        path = getProjectPath() + "/doc/samples_console.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()
        myFlow.close()


    def test_mask(self):
        path = getProjectPath() + "/doc/masking_console.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()
        myFlow.close()

    def test_mapping(self):
        path = getProjectPath() + "/doc/mapping_console.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()
        myFlow.close()

    def test_SQL_1(self):
        path = getProjectPath() + "/doc/csv_input_sql_translate.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()
        myFlow.close()

    def test_while(self):
        path = getProjectPath() + "/doc/while_console.json"
        myFlow: Flow = FlowManager.read(path) \
            .set_param({"file_name": "F:/07_数据源大全/store_order/channel.csv",
                        "while_var": 0}
                       )
        myFlow.run()
        myFlow.close()

    def test_rename(self):
        path = getProjectPath() + "/doc/rename_console.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()
        myFlow.close()

    def test_markdown(self):
        path = getProjectPath() + "/doc/rename_markdown.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()
        myFlow.close()


    def test_SQL(self):
        path = getProjectPath() + "/doc/faker_input_sql_translate.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()
        myFlow.close()

    # 自定义插件功能
    def test_Hello(self):
        path = "../doc/hello_input_console.json."
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()
        myFlow.close()

    def test_filter(self):
        path = getProjectPath() + "/doc/faker_input_filter_console.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()
        myFlow.close()

    def test_for(self):
        path = getProjectPath() + "/doc/faker_input_console_for.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()
        myFlow.close()

    def test_for2(self):
        path = getProjectPath() + "/doc/mysql_input_for_mysql_input.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()
        myFlow.close()

    def test_for3(self):
        path = getProjectPath() + "/doc/mysql_input_for_mysql_output.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()
        myFlow.close()


if __name__ == '__main__':
    unittest.main()
