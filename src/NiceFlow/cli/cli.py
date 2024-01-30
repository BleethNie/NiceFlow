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
@click.option("--db_path", default="", help="输入duckdb数据库的路径，不存在则为内存模式[可选]")
@click.option("--res_path", default="", help="输入文件路径，该路径下的文件会被自动加载到db中[可选]")
@click.option("--function_path", default="", help="输入函数路径，该路径为python文件,可以作为数据库自定义函数使用[可选]")
def sql(sql_script: str, db_path: str = None, res_path: str = None, function_path: str = None):
    if db_path:
        con = duckdb.connect(db_path)
    else:
        con = duckdb.connect()
    # 自动加载目录下的res文件
    if res_path:
        for file in os.listdir(res_path):
            table_path = res_path+"/"+file
            table_name = file.split(".")[0]
            if file.endswith(".csv"):
                con.sql(f'''
                drop table if EXISTS  {table_name};
                CREATE TABLE {table_name} AS SELECT * FROM read_csv_auto('{table_path}',header = true);
                ''')
            if file.endswith(".parquet"):
                con.sql(f'''
                drop table if EXISTS  {table_name};
                CREATE TABLE {table_name} AS SELECT * FROM read_parquet('{table_path}');
                ''')
            if file.endswith(".xlsx"):
                con.sql(f'''
                drop table if EXISTS  {table_name};
                CREATE TABLE {table_name} AS SELECT * FROM st_read('{table_path}');
                ''')
    if function_path:
        module = load_module(function_path)
        items = inspect.getmembers(module, inspect.isfunction)
        for item in items:
            con.create_function(item[0],item[1])
    duck_df = con.sql(sql_script)
    df =  duck_df.to_df()
    con.close()
    return df


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


if __name__ == '__main__':
    sql_script = '''
    copy  (select f_print(d_date) from msd_2024 where d_date = '2023-12-31') to  'C:/Users/xiaow/Desktop/22/test/2.csv';
    select f_print(d_date) from msd_2024 where d_date = '2023-12-31';
    '''
    duck_df = sql(sql_script,db_path=None,
                  res_path="C:/Users/xiaow/Desktop/22/test",
                  function_path="C:/Users/xiaow/Desktop/22/test/common_function.py")
    print(duck_df)
