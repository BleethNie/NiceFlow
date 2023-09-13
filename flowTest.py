from core.flow import Flow
from core.manager import FlowManager

def test2():
    path = "E:/02_Resource/01_Code/python/EasyFlow/doc/1.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()

def test1():
    path = "E:/02_Resource/01_Code/python/EasyFlow/doc/parquet_input_console.json"
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()

if __name__ == '__main__':
    test1()
