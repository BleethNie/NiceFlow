import json
from datetime import datetime

from sqlalchemy import create_engine, text

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin


class MySQLOutput(IPlugin):

    def init(self, param: json, flow: Flow):
        super(MySQLOutput, self).init(param, flow)

    def execute(self):
        super(MySQLOutput, self).execute()

        host = self.param.get("host", "127.0.0.1")
        port = self.param.get("port", 3306)
        db = self.param.get("db", "")
        user = self.param.get("username", "root")
        password = self.param.get("password", "123456")
        table = self.param.get("table", "")
        write_method = self.param.get("write_method", "insert")
        update_keys = self.param.get("update_keys", [])
        encode_order = self.param.get("encode_order", "")

        temp_table = f'__{table}_{datetime.now().strftime("%Y%m%d%H%M%S")}'
        # 获取上一步结果
        pre_node = self.pre_nodes[0]
        duck_df = self._pre_result_dict[pre_node.name]

        # 写数据库
        engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8'
                               % (user, password, host, port, db))
        duck_df.to_df().to_sql(temp_table, con=engine, chunksize=10000, if_exists='replace', index=False,
                               index_label=id)

        # 设置表编码
        if len(encode_order) != 0:
            with engine.connect() as conn:
                conn.execute(
                    text(f"ALTER TABLE {temp_table}  CONVERT TO CHARACTER SET utf8mb4 COLLATE {encode_order};"))

        # 判断sql
        update_field_sql = ""
        for key in update_keys:
            update_field_sql = update_field_sql + f"  l_table.{key}=r_table.{key} and  "
        if len(update_field_sql) != 0:
            update_field_sql = update_field_sql.removesuffix("and  ")

        set_sql = ""
        columns = duck_df.columns
        for key in columns:
            set_sql = set_sql + f"  l_table.{key}=r_table.{key} ,  "
        if len(set_sql) != 0:
            set_sql = set_sql.removesuffix(",  ")

        # 写入实际的表中,表不存在则自动创建
        #  insert/只插入数据[无主键则全部插入，有主键则根据主键判断是否插入]
        #  update/只更新数据[需要更新键]
        #  overwrite/清空数据并导入[不需要数据]
        #  merge/根据主键判断是更新或者插入[必须有主键]

        with engine.connect() as conn:
            # 创建 {table}如果不存在
            conn.execute(text(f"create table if not exists {table} like {temp_table}"))

            if write_method == "update":
                update_sql = f"update  {table} l_table inner join {temp_table} r_table on {update_field_sql}  set {set_sql} ;"
                conn.execute(text(update_sql))
            elif write_method == "overwrite":
                conn.execute(text(f"truncate table {table}"))
                conn.execute(text(f"insert into {table} select * from {temp_table}"))
            elif write_method == "merge":
                insert_sql = f'insert into {table} select * from {temp_table} l_table where not exists (select 1 from {table} r_table where   {update_field_sql} ) ;'
                update_sql = f"update  {table} l_table inner join {temp_table} r_table on {update_field_sql}  set {set_sql} ;"
                conn.execute(text(insert_sql))
                conn.execute(text(update_sql))
            else:
                # 默认使用insert
                conn.execute(text(f"insert into {table} select * from {temp_table}"))
            # 删除临时表
            conn.execute(text(f"drop table {temp_table}"))

        self.set_result(None)

    def to_json(self):
        super(MySQLOutput, self).to_json()
