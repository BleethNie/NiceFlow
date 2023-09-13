# 指定文件夹路径
from core.flow import Flow
from core.manager import FlowManager

if __name__ == '__main__':
    a:Flow = FlowManager.read("E:/02_Resource/01_Code/python/EasyFlow/doc/1.json")
    a.run()