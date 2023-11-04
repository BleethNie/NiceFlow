# 命令行工具
import json
import re
import click

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager
from NiceFlow.core.utils.encrypt_data import EncryptData


@click.group()
def cli():
    """A simple command line tool."""


@cli.command('exec', short_help='exec flow task')
@click.option("--path", default="", help="input your task json file path")
def init(path: str):
    print("path:", path)
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()


@cli.command('explore', short_help='explore a data info')
def explore():
    pass


@cli.command('chart', short_help='chart a data ')
def chart():
    pass


# @cli.command('encrypt', short_help='encrypt a task flow password config')
# @click.option("--path", default="", help="input your task json file path")
# @click.password_option()
def encrypt(path: str, password: str):
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
        json.dump(flow_json, fp, indent=4, ensure_ascii=False)


# @cli.command('decrypt', short_help='decrypt a task flow password config')
# @click.option("--path", default="", help="input your task json file path")
# @click.password_option()
def decrypt(path: str, password: str):
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
                    decrypt_content =re.findall("AES\\((.*)\\)", value)[0]
                    decrypt = eg.decrypt(decrypt_content)
                    if decrypt is None:
                        return
                    node_properties[key] = decrypt
    with open(path, 'w', encoding='utf8') as fp:
        json.dump(flow_json, fp, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    encrypt("E:\\02_Resource\\01_Code\\python\\NiceFlow\\NiceFlow\\doc\\1.json", "1234567")
    decrypt("E:\\02_Resource\\01_Code\\python\\NiceFlow\\NiceFlow\\doc\\1.json", "123456")
