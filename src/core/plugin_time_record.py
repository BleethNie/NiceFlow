import time

from src.core.plugin import IPlugin
from loguru import  logger

class PluginTimeRecord:

    def __init__(self, plugin: IPlugin):
        self.plugin = plugin
        self.__start_time = None
        self.__end_time = None
        self.__run_count = 0

    def stop(self):
        self.__end_time = time.time()

    def start(self):
        self.__run_count = self.__run_count+1
        self.__start_time = time.time()

    # 打印本次执行时间记录
    def print(self) :
        start = time.localtime(self.__start_time)
        end = time.localtime(self.__end_time)
        start_format = time.strftime("%Y-%m-%d %H:%M:%S", start)
        end_format = time.strftime("%Y-%m-%d %H:%M:%S", end)
        run_time = int(round(self.__end_time * 1000))-int(round(self.__start_time * 1000))
        run_time = round(run_time/1000,3)
        df_count = self.plugin.df_count

        logger.info(f"【{self.plugin.id}】/【{self.plugin.name}】执行第【{self.__run_count}】次，"
              f"执行开始时间为【{start_format}】，结束时间为【{end_format}】,"
              f"执行耗时【{run_time}】,处理数据量为【{df_count}】")
