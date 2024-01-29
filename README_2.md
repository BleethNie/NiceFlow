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
pip install E:\02_Resource\01_Code\python\NiceFlow\NiceFlow\dist\NiceFlow-0.0.2-py3-none-any.whl
```



### 分布式

#### 角色

- master:分配任务者
- worker:任务执行者
- operator:任务开发者

#### 任务执行

- 手动指定任务
- master分配任务

#### 定时器工具

### 场景

#### 数据清洗

#### 数据分析

#### 数据管理

#### 报表展示

#### 大数据数据同步

#### 数据迁移

#### 作为工具使用不同数据间转换

- 需要打包发布
-

#### 爬虫

### 程序打包发布

### 数据资源

- 可以用来做示例对比 https://github.com/TurboWay/bigdata_analyse
- 地铁人流量数据 https://github.com/geekyouth/SZT-bigdata/blob/master/.file/2018record3.zip

### 二次开发

- 后台管理    https://gitee.com/likeadmin/likeadmin_python?_from=gitee_search
- sql编辑器   https://github.com/pinterest/querybook
- 报表       https://github.com/lightdash/lightdash
- 报表       https://github.com/getredash/redash





## 使用

```shell
#打包
python setup.py bdist_wheel

#安装
conda activate test_flow

pip install NiceFlow-0.0.1-py3-none-any.whl


twine upload --repository pypi dist/*

```


六、使用setup.py安装包
python setup.py install 将模块安装到全局环境中

python setup.py develop 创建一个软链接指向实际所在目录，不会真正安装

七、如何发布到PyPI
注册PyPI账号，创建~/.pypirc文件，配置PyPI访问地址和账号。

python setup.py register sdist upload -r http://pypi.org 使用该信息注册

python setup.py upload 上传源码包