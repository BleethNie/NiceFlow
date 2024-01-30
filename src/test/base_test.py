import inspect
from datetime import datetime, timedelta
import unittest

# 导入datetime模块，用于获取当前时间
import datetime
# 导入time模块，用于休眠
import time

from NiceFlow.common.module_util import load_module


class TestBase(unittest.TestCase):

    def test_base(self):

        # 获取当前时间，格式为年-月-日 时:分:秒
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 打印当前时间
        print("当前时间为:", now)
        # 获取当前时间的分钟
        minute = int(now[-5:-3])
        # 获取当前时间分钟的尾数
        tail = minute % 10
        # 判断当前时间分钟的尾数是否为0-9
        if 0 <= tail <= 9:
            # 计算休眠的时间，单位为秒
            sleep_time = (10 - tail) * 60
            # 打印休眠的时间
            print("休眠", sleep_time, "秒")
            # 休眠
            time.sleep(sleep_time)
        else:
            # 打印不需要休眠
            print("不需要休眠")


    def test_base2(self):

        # 获取当前时间，格式为年-月-日 时:分:秒
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 打印当前时间
        print("当前时间为:", now)
        # 获取当前时间的分钟
        minute = int(now[-5:-3])
        # 获取当前时间分钟的尾数
        tail = minute % 10
        # 判断当前时间分钟的尾数是否为0-9
        if 0 <= tail <= 9:
            # 计算休眠的时间，单位为秒
            sleep_time = (10 - tail) * 60
            # 打印休眠的时间
            print("休眠", sleep_time, "秒")
            # 休眠
            time.sleep(sleep_time)
        else:
            # 打印不需要休眠
            print("不需要休眠")

    def test_base3(self):
        m = load_module("C:/Users/xiaow/Desktop/common_function.py")
        items = inspect.getmembers(m, inspect.isfunction)
        for item in items:
            print(item[1])

if __name__ == '__main__':
    unittest.main()
