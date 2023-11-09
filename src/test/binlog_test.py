import unittest

from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import DeleteRowsEvent, UpdateRowsEvent, WriteRowsEvent


# https://blog.csdn.net/u012429202/article/details/132151332
class TestMySQLBinlog(unittest.TestCase):

    def test_read_binlog(self):
        mysql_connect = {
            "host": "127.0.0.1",
            "port": 3306,
            "user": "root",
            "passwd": "123456"
        }
        stream = BinLogStreamReader(
            connection_settings=mysql_connect,
            server_id=3,  # slave标识，唯一
            blocking=True,  # 阻塞等待后续事件
            resume_stream=False,  # True为从最新位置读取, 默认False
            # 设定只监控写操作：增、删、改
            only_events=[
                DeleteRowsEvent,
                UpdateRowsEvent,
                WriteRowsEvent
            ],
        )
        for event in stream:
            event.dump()  # 打印所有信息


if __name__ == '__main__':
    unittest.main()
