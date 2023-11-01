import os

from src.core.flow import Flow
from src.core.manager import FlowManager


def baseTest():
    path = "../doc/1.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()


def parquetTest():
    path = "..../doc/parquet_input_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()


def fakerTest():
    path = "..../doc/faker_input_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()


def sortTest():
    path = "../doc/sort_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()


def samplesTest():
    path = "../doc/samples_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()


def httpTest():
    path = "../doc/http_input_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()


def maskTest():
    path = "../doc/masking_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()


def mappingTest():
    path = "../doc/mapping_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()

def SQLTest2():
    path = "../doc/csv_input_sql_translate.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()

def whileTest():
    path = "../doc/while_console.json"
    myFlow: Flow = FlowManager.read(path) \
        .set_param({"file_name": "F:/07_数据源大全/store_order/channel.csv",
                    "while_var": 0}
                   )
    myFlow.run()
    myFlow.close()


def renameTest():
    path = "../doc/rename_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()


def markdownTest():
    path = "../doc/rename_markdown.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()


def httpOutputTest():
    path = "../doc/http_output_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()


def ckOutputTest():
    path = "../doc/sort_ck.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()

def ckInputTest():
    path = "../doc/ck_input_ck_output.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()


def SQLTest():
    path = "../doc/faker_input_sql_translate.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()

# 自定义插件功能
def HelloTest():
    path = "../doc/hello_input_console.json."
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()

def csvInput_CKOutputTest():
    path = "../doc/csv_input_ck_output.json"
    data_dir = "F:\\07_数据源大全\\车站数据\\后两周的数据"
    file_list = os.listdir(data_dir)
    for file in file_list:
        myFlow: Flow = FlowManager.read(path).set_param({"file_name": data_dir+"\\"+file})
        myFlow.run()
        myFlow.close()


if __name__ == '__main__':
    HelloTest()
