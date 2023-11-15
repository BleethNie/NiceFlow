import json
import logging

import pymysql



class MySQLDBLogHandler(logging.Handler):
    """
    CREATE TABLE `flow_log` (
      `id` bigint NOT NULL AUTO_INCREMENT,
      `thread_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
      `repr` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
      `level_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
      `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
      `function` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
      `line` int DEFAULT NULL,
      `message` varchar(255) DEFAULT NULL,
      `file_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
      `content` varchar(255) DEFAULT NULL,
       PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

   自定义logging.Handler模块，自定义将日志输出到指定位置(这里是输出到DuckDB)
   """

    def __init__(self, host="127.0.0.1", port=3306, username="root", password="123456",
                 db="che", table="flow_log"):
        super(MySQLDBLogHandler, self).__init__()
        self.db = pymysql.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=db)  # 连接地址，登陆名，密码，数据库标示
        self.table = table  # 表名
        self.cursor = self.db.cursor()
        self.db.commit()

    def emit(self, record: logging.LogRecord):
        """
        重写logging.Handler的emit方法
        :param record: 传入的日志信息
        :return:
        """
        # 对日志信息进行格式化
        msg = record.msg
        msg_json = json.loads(msg)

        kwargs = {
            "content": msg_json["text"],
            "repr": msg_json["record"]["time"]["repr"],
            "thread_name": msg_json["record"]["thread"]["name"],
            "name": msg_json["record"]["name"],
            "function": msg_json["record"]["function"],
            "message": msg_json["record"]["message"],
            "line": msg_json["record"]["line"],
            "level_name": msg_json["record"]["level"]["name"],
            "file_name": msg_json["record"]["file"]["name"]
        }
        keys = list(kwargs.keys())
        for i in range(len(keys)):
            keys[i] = '`' + keys[i] + '`'
        keys = ','.join(keys)
        values = ','.join(['%s'] * len(kwargs))
        sql_insert = f"INSERT INTO {self.table}({keys}) VALUES ({values})"
        self.db.ping(reconnect=True)  # 测试数据库连接
        try:
            self.cursor.execute(sql_insert, tuple(kwargs.values()))
            self.db.commit()
        except Exception as err:
            print('插入错误', err)
