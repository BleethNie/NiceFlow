import glob
import os

# 指定文件夹路径
from core.manager import PluginManager

if __name__ == '__main__':
    PluginManager.discover_plugins()
    PluginManager.get_register_plugins()
    PluginManager.execute_plugin("CsvInput")
