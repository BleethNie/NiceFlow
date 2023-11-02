# 命令行工具
import click
from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


@click.command()
@click.option("--path", default="admin", help="input your name")
def run(path: str):
    print("path:", path)
    myFlow: Flow = FlowManager.read(path)
    myFlow.run()
    myFlow.close()


if __name__ == '__main__':
    run("nice")
