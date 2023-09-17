from core.flow import Flow
from core.manager import FlowManager


def baseTest():
    path = "E:/02_Resource/01_Code/python/EasyFlow/doc/1.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()


def parquetTest():
    path = "E:/02_Resource/01_Code/python/EasyFlow/doc/parquet_input_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()


def fakerTest():
    path = "E:/02_Resource/01_Code/python/EasyFlow/doc/faker_input_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()


def sortTest():
    path = "E:/02_Resource/01_Code/python/EasyFlow/doc/sort_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()


def samplesTest():
    path = "E:/02_Resource/01_Code/python/EasyFlow/doc/samples_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()


# TODO: 未完成
def httpTest():
    path = "E:/02_Resource/01_Code/python/EasyFlow/doc/http_input_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()


def maskTest():
    path = "E:/02_Resource/01_Code/python/EasyFlow/doc/masking_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()


# TODO: 未完成
def mappingTest():
    path = "E:/02_Resource/01_Code/python/EasyFlow/doc/mapping_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()


def whileTest():
    path = "E:/02_Resource/01_Code/python/EasyFlow/doc/while_console.json"
    myFlow: Flow = FlowManager.read(path) \
        .set_param({"file_name": "F:/07_数据源大全/store_order/channel.csv",
                    "while_var": 0}
                   )
    myFlow.run()
    myFlow.close()

def renameTest():
    path = "E:/02_Resource/01_Code/python/EasyFlow/doc/rename_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()

def markdownTest():
    path = "E:/02_Resource/01_Code/python/EasyFlow/doc/rename_markdown.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()

if __name__ == '__main__':
    fakerTest()
