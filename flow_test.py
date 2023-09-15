from core.flow import Flow
from core.manager import FlowManager


def paramTest():
    path = "E:/02_Resource/01_Code/python/EasyFlow/doc/flow/flow_param_console.json"
    myFlow: Flow = FlowManager.read(path)
    flow_param = {
        "file_name": "F:/07_数据源大全/store_order/channel.csv",
        "row": 20
    }
    myFlow.set_param(flow_param)
    myFlow.run()


if __name__ == '__main__':
    paramTest()
