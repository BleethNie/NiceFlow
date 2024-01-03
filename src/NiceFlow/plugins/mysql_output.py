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
        write_method = self.param.get("write_method", "")
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

        # 写入实际的表中,表不存在则自动创建
        #  insert/只插入数据[无主键则全部插入，有主键则根据主键判断是否插入]
        #  update/只更新数据[需要更新键]
        #  overwrite/清空数据并导入[不需要数据]
        #  merge/根据主键判断是更新或者插入[必须有主键]

        # 创建 {table}如果不存在
        engine.execute(f"create table if not exists {table} like {temp_table}")

        # 判断sql
        update_sql = ""
        for key in  update_keys:
            update_sql =update_sql+f"  l_table.{key}=r_table.{key} and  "
        if len(update_sql)!= 0:
            update_sql = update_sql.removesuffix("and  ")

        set_sql = ""
        columns = duck_df.columns
        for key in  columns:
            set_sql =set_sql+f"  l_table.{key}=r_table.{key} ,  "
        if len(set_sql)!= 0:
            set_sql = set_sql.removesuffix(",  ")

        if write_method == "update":
            engine.execute(f"update {table} set * from {temp_table}")
        elif write_method == "overwrite":
            engine.execute(f"truncate table {table}")
            engine.execute(f"insert into {table} select * from {temp_table}")
        elif write_method == "merge":
            engine.execute(f'insert into {table} select * from {temp_table} l_table where not exists (select 1 from {table} r_table where   {update_sql} ) ;')
            engine.execute(f"update  {table} set {set_sql}   from {temp_table} r_table join {table} l_table on {update_sql} ;")
        else:
            # 默认使用insert
            engine.excute(f"insert into {table} select * from {temp_table}")

        # 删除临时表
        engine.execute(f"drop table {temp_table}")

    def to_json(self):
        super(MySQLOutput, self).to_json()
