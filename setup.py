from setuptools import setup, find_packages
import os


# 读取文件
def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


setup(
    # 基本信息
    name="NiceFlow",  # 项目名，确定唯一，不然上传 pypi 会失败
    version="0.0.1",  # 项目版本
    author='BleethNie',  # 开发者
    author_email='xiao5406710@foxmail.com',  # 开发者邮箱
    description='ETL数据处理/数据迁移/数据分析工具',  # 摘要描述
    long_description=read_file('README.md'),  # 详细描述，一般用于 pypi 主页展示
    long_description_content_type="text/markdown",  # 详细描述的文件类型
    platforms='python3',  # 项目支持的平台
    url='https://www.xx.cn',  # 项目主页

    # 项目配置
    # 包含所有src文件夹下的包，但排除tests包
    packages=find_packages('src', exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
    package_dir={'': 'src'},  # find_packages指定了文件夹后，这里也需要配置
    include_package_data=True,
    package_data={
        # 任何包中含有.txt文件，都包含它
        '': ['*.txt']

    },
    exclude_package_data={
        # 忽略demo01包下的data文件夹里的abc.txt文件
        'demo01': ['data/abc.txt']
    },
    # 支持Python版本
    python_requires='>=3.8',
    # 表明当前模块依赖哪些包，若环境中没有，则会从pypi中下载安装
    install_requires=[
        'duckdb >= 0.8.1',
        'pandas >= 2.1.0',
        'pyarrow >= 13.0.0',
        'loguru >= 0.7.2',
        'click>=8.1.7',
        'Faker>=19.6.1',
        'blinker>=1.7.0',
        'sqlglot>=19.1.0'
    ],
    # 用来支持自动生成脚本，如下配置
    # 在类Unix系统下，会在 /usr/local/bin下生成 NiceFlow 命令
    entry_points={
        'console_scripts': [
            'NiceFlow = NiceFlow.cli.cli:cli',  # 入口指向demo01包下的first文件里的 test1 函数
        ],
    }
)