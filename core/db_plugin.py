import abc
import json
from typing import List, Dict

import duckdb

from core.tool import extract_variable


class DBPlugin():

    def create_table(self):
        # 支持自动建表
        pass

    def write_table(self):
        # 写入数据库
        pass

    def read_table(self):
        # 从数据库读取数据
        pass
