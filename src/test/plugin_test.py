import os

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager

def getProjectPath()->str:
    # 获取当前文件的绝对路径
    current_file = os.path.abspath(__file__)
    # 获取当前文件所在目录的绝对路径
    current_directory = os.path.dirname(current_file)
    # 获取当前项目的根目录
    project_root = os.path.dirname(os.path.dirname(current_directory))
    return project_root

def baseTest():
    path = getProjectPath()+"/doc/1.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()


def parquetTest():
    path = getProjectPath()+"/doc/parquet_input_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()


def fakerTest():
    path = getProjectPath()+"/doc/faker_input_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()


def sortTest():
    path = getProjectPath()+"/doc/sort_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()


def samplesTest():
    path = getProjectPath()+"/doc/samples_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()


def httpTest():
    path = getProjectPath()+"/doc/http_input_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()


def maskTest():
    path = getProjectPath()+"/doc/masking_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()


def mappingTest():
    path = getProjectPath()+"/doc/mapping_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()

def SQLTest2():
    path = getProjectPath()+"/doc/csv_input_sql_translate.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()

def whileTest():
    path = getProjectPath()+"/doc/while_console.json"
    myFlow: Flow = FlowManager.read(path) \
        .set_param({"file_name": "F:/07_数据源大全/store_order/channel.csv",
                    "while_var": 0}
                   )
    myFlow.run()
    myFlow.close()


def renameTest():
    path = getProjectPath()+"/doc/rename_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()


def markdownTest():
    path = getProjectPath()+"/doc/rename_markdown.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()


def httpOutputTest():
    path = getProjectPath()+"/doc/http_output_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()


def ckOutputTest():
    path = getProjectPath()+"/doc/sort_ck.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()

def ckInputTest():
    path = getProjectPath()+"/doc/ck_input_ck_output.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()


def SQLTest():
    path = getProjectPath()+"/doc/faker_input_sql_translate.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()

# 自定义插件功能
def HelloTest():
    path = "../doc/hello_input_console.json."
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()


# 自定义插件功能
def CsvOutput():
    path = getProjectPath()+"/doc/faker_input_csv_output.json."
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()

def csvInput_CKOutputTest():
    path = getProjectPath()+"/doc/csv_input_ck_output.json"
    data_dir = "F:\\07_数据源大全\\车站数据\\后两周的数据"
    file_list = os.listdir(data_dir)
    for file in file_list:
        myFlow: Flow = FlowManager.read(path).set_param({"file_name": data_dir+"\\"+file})
        myFlow.run()
        myFlow.close()


if __name__ == '__main__':
    CsvOutput()
