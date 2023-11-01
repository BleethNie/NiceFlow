# 命令行工具
import click
from core.flow import Flow

from core.manager import FlowManager


@click.command()
@click.option("--name", default="admin", help="input your name")
def run(name:str):
    path = "../../doc/hello_input_console.json."
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()
    print("nice:",name)
