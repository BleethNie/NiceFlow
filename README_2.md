## NiceFlow

> 类似Kettle工具，主要实现数据ETL处理

### 使用

#### python环境

python 3.10

#### 安装使用

- 先打包
```shell

python setup.py bdist_wheel

```

- 先卸载
```shell

pip uninstall NiceFlow
```

- 再安装新的
```shell
pip install E:\02_Resource\01_Code\python\NiceFlow\NiceFlow\dist\NiceFlow-0.0.1-py3-none-any.whl
```


- 使用命令行工具测试 1.json 是Faker组件输出到Console
```shell
NiceFlow --path 1.json
```

- 使用命令行工具测试 2.json 是Faker组件输出到CsvOutput
```shell
NiceFlow --path 2.json
```
-- 
