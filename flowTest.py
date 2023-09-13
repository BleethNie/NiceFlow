from core.flow import Flow
from core.manager import FlowManager

if __name__ == '__main__':
    myFlow: Flow = FlowManager.read("E:/02_Resource/01_Code/python/EasyFlow/doc/1.json")
    myFlow.run()
