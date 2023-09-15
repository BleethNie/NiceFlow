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


if __name__ == '__main__':
    sortTest()
