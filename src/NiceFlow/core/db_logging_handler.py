import json
import logging
from queue import Queue


class DuckDBLogHandler(logging.Handler):
    """
   自定义logging.Handler模块，自定义将日志输出到指定位置(这里是输出到DuckDB)
   """

    def __init__(self, path="",table_name=""):
        super(DuckDBLogHandler, self).__init__()
        self.queue = Queue()

    def emit(self, record):
        """
        重写logging.Handler的emit方法
        :param record: 传入的日志信息
        :return:
        """
        # 对日志信息进行格式化
        value = self.format(record)
        # 转成json格式，注意ensure_ascii参数设置为False，否则中文乱码
        value = json.dumps(value, ensure_ascii=False).encode("utf-8")
        print(value)
        aa = logging.StreamHandler()