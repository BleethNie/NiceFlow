# 命令行工具
import inspect
import json
import re
import click
import duckdb
import os
from loguru import logger

from NiceFlow.common.module_util import load_module
from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


@click.group()
def cli():
    """A simple command line tool."""
    pass


@cli.command('exec', short_help='exec flow task')
@click.option("--path", default="", help="input your task json file path")
@click.option("--param", default="{}", help="动态参数,为一个json格式的字符串")
def init(path: str, param: str):
    cmd = os.getcwd()
    real_path = cmd + "/" + path
    logger.info(f"real path is : {real_path}")
    myFlow: Flow = FlowManager.read(real_path)
    logger.info(f"param is: {param}")
    myFlow.set_param(json.loads(param))
    myFlow.run()


@cli.command('explore', short_help='explore a data info')
def explore():
    pass


@cli.command('sql', short_help='sql a data ')
@click.option("--sql_script", default="", help="sql脚本语句，支持多行")
@click.option("--sql_path", default="", help="sql脚本文件")
@click.option("--db_path", default="", help="输入duckdb数据库的路径，不存在则为内存模式[可选]")
@click.option("--res_path", default="", help="输入文件路径，该路径下的文件会被自动加载到db中[可选]")
@click.option("--function_path", default="", help="输入函数路径，该路径为python文件,可以作为数据库自定义函数使用[可选]")
@click.option("--result_path", default="", help="输入结果路径,支持csv,json,parquet,txt,excel,clipboard当输入为clipboard时,结果直接写入剪贴板")
@click.option("--is_overwrite", default="False", help="是否重新加载数据")
@click.option("--all_varchar", default="", help="是否全为varchar类型")
def sql(sql_script: str = None, sql_path: str = None, db_path: str = None, res_path: str = None,
        function_path: str = None, result_path: str = None, is_overwrite=False, all_varchar=False):
    if db_path:
        con = duckdb.connect(db_path)
    else:
        con = duckdb.connect()
    # 自动加载目录下的res文件
    if res_path:
        for file in os.listdir(res_path):
            table_path = res_path + "/" + file
            if len(file.split(".")) <= 1:
                continue
            table_name = file.split(".")[0]
            file_suffix = file.split(".")[1]

            # 表存在并且不是覆盖模式，则跳过
            table_name_result = con.execute(f'''SELECT * FROM sqlite_master WHERE type='table' AND name='{table_name}';''')
            if is_overwrite is False and len(table_name_result.fetchall()) > 0:
                continue

            # 表需要重新加载
            if file_suffix.lower() == "csv":
                con.sql(f'''
                drop table if EXISTS  {table_name};
                CREATE TABLE {table_name} AS SELECT * FROM read_csv_auto('{table_path}',header = true,ALL_VARCHAR={all_varchar});
                ''')
            if file_suffix.lower() == "parquet":
                con.sql(f'''
                drop table if EXISTS  {table_name};
                CREATE TABLE {table_name} AS SELECT * FROM read_parquet('{table_path}');
                ''')
            if file_suffix.lower() == "xlsx":
                con.sql(f'''
                INSTALL spatial;
                LOAD spatial;
                drop table if EXISTS  {table_name};
                CREATE TABLE {table_name} AS SELECT * FROM st_read('{table_path}');
                ''')
            if file_suffix.lower() == "json":
                con.sql(f'''
                drop table if EXISTS  {table_name};
                CREATE TABLE {table_name} AS SELECT * FROM read_json('{table_path}',auto_detect=true);
                ''')
    # 加载自定义函数
    if function_path:
        module = load_module(function_path)
        items = inspect.getmembers(module, inspect.isfunction)
        for item in items:
            con.create_function(item[0], item[1])
    #
    if sql_script:
        duck_df = con.sql(sql_script)
    else:
        with open(sql_path, "r", encoding='utf8') as f:
            duck_df = con.sql(f.read())

    if duck_df is not None:
        duck_df.show(max_width=1000, max_rows=100)
        df = duck_df.to_df()
        logger.info(f"查询结果总数为：{len(df)}")
        if result_path:
            result_path = result_path.strip()
            if result_path.endswith(".csv"):
                df.to_csv(result_path, index=False)
            elif result_path.endswith(".xlsx"):
                df.to_excel(result_path, index=False)
            elif result_path.endswith(".json"):
                df.to_json(result_path, index=False)
            elif result_path.endswith(".parquet"):
                df.to_parquet(result_path, index=False)
            elif result_path.endswith("clipboard"):
                logger.info(f"文件已经写入剪贴板")
                df.to_clipboard()
    con.close()


@cli.command('chart', short_help='chart a data ')
def chart():
    pass


@cli.command('encrypt', short_help='encrypt a task flow password config')
@click.option("--path", default="", help="input your task json file path")
@click.password_option()
def encrypt(path: str, password: str):
    from NiceFlow.core.utils.encrypt_data import EncryptData

    eg = EncryptData(password)
    with open(path, 'r', encoding='utf8') as fp:
        flow_json = json.load(fp)
        nodes_array: json = flow_json["nodes"]
        # 组装node,edge
        for node_json in nodes_array:
            node_properties: json = node_json["properties"]
            items = node_properties.items()
            for key, value in items:
                if key in ["password", "passwd"]:
                    encrypt_data = eg.encrypt(value)
                    node_properties[key] = "AES({})".format(encrypt_data)
    with open(path, 'w', encoding='utf8') as fp:
        json.dump(flow_json, fp, indent=2, ensure_ascii=False)


@cli.command('decrypt', short_help='decrypt a task flow password config')
@click.option("--path", default="", help="input your task json file path")
@click.password_option()
def decrypt(path: str, password: str):
    from NiceFlow.core.utils.encrypt_data import EncryptData

    eg = EncryptData(password)
    with open(path, 'r', encoding='utf8') as fp:
        flow_json = json.load(fp)
        nodes_array: json = flow_json["nodes"]
        # 组装node,edge
        for node_json in nodes_array:
            node_properties: json = node_json["properties"]
            items = node_properties.items()
            for key, value in items:
                if key in ["password", "passwd"]:
                    decrypt_content = re.findall("AES\\((.*)\\)", value)[0]
                    decrypt = eg.decrypt(decrypt_content)
                    if decrypt is None:
                        return
                    node_properties[key] = decrypt
    with open(path, 'w', encoding='utf8') as fp:
        json.dump(flow_json, fp, indent=2, ensure_ascii=False)



@cli.command('serve', short_help='启动server服务')
@click.password_option()
def serve():

    pass



@cli.command('client', short_help='客户端可以提交任务到服务端，查看服务端相关内容')
@click.password_option()
def decrypt(path: str, password: str):
    from NiceFlow.core.utils.encrypt_data import EncryptData

    eg = EncryptData(password)
    with open(path, 'r', encoding='utf8') as fp:
        flow_json = json.load(fp)
        nodes_array: json = flow_json["nodes"]
        # 组装node,edge
        for node_json in nodes_array:
            node_properties: json = node_json["properties"]
            items = node_properties.items()
            for key, value in items:
                if key in ["password", "passwd"]:
                    decrypt_content = re.findall("AES\\((.*)\\)", value)[0]
                    decrypt = eg.decrypt(decrypt_content)
                    if decrypt is None:
                        return
                    node_properties[key] = decrypt
    with open(path, 'w', encoding='utf8') as fp:
        json.dump(flow_json, fp, indent=2, ensure_ascii=False)





if __name__ == '__main__':
    sql_script = '''
    select * from total_RQ_DEVICE_20240130;
    '''
    duck_df = sql(sql_script, db_path=None,
                  res_path="C:/Users/xiaow/Desktop/22/test",
                  function_path="C:/Users/xiaow/Desktop/22/test/common_function.py",
                  # result_path="C:/Users/xiaow/Desktop/22/test/result.csv"
                  # result_path="C:/Users/xiaow/Desktop/22/test/result.csv"
                  )
