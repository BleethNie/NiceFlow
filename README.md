## NiceFlow

> 类似Kettle工具，主要实现数据ETL处理

### 使用

#### python环境

> 在 python 3.10上开发

#### 安装依赖

```shell
pip install -r requirement.txt
```

#### 测试案例

- plugin_test.py 测试插件功能
- flow_test.py 测试flow功能


#### cli使用

```shell
pip install NiceFlow

# 执行flow任务
NiceFlow exec --path csv_input_ck_output.json
```

### 架构图

TODO

### 插件

#### 输入

| 插件            | 功能         | 类型  | 完成情况 | 文档  |
|---------------|------------|-----|------|---------|
| Starter       | 启动器        |     | 完成   |       |
| CSVInput      | 读取CSV数据    |     | 完成   |      |
| FakerInput    | 假数据生成      |     | 完成   |      |
| ExcelInput    |            |     | 完成   |      |
| ParquetInput  |            |     | 完成   |      |
| MySQLInput    |            |     | 完成     |      |
| ESInput       |            |     |      |      |
| DorisInput    |            |     |      |      |
| SQLiteInput   |            |     |      |      |
| PostgrestInput|            |     |      |      |
| HiveInput     |            |     |      |      |
| PulsarInput   |            |     |      |      |
| PaimonInput   |            |     |      |      |
| IceBergInput  |            |     |      |      |
| CKInput       | CK数据读取     |     | 完成   |      |
| KafkaInput    |            |     |      |      |
| MqttInput     |            |     |      |      |
| OracleInput   |            |     |      |      |
| SqlserverInput |            |     |      |      |
| FlinkCDCInput |            |     |      |      |
| MongoInput    |            |     | 完成   |      |
| DuckDBInput   |            |     | 完成   |      |
| HttpInput     | Http读      |     | 完成   |      |
| HtmlInput     | 读取Html中的表格 |     |      |      |

#### 输出

| 插件             | 功能            | 类型   | 完成情况 | 文档  |
|----------------|---------------|--------|----------|-----|
| Console  | 控制台打印         |        | 完成      |     |
| CKOutput       | CK数据写入        |        | 完成      |     |
| HttpOutput     | Http写         |        |     完成     |     |
| CSVOutput      | CSV输出/切分文件    |      | 完成       |     |
| HtmlOutput     | 将df写出到html    |      |        |     |
| MarkdownOutput | 数据写出到markdown |     |   完成       |     |

#### 转换

| 插件          | 功能        | 类型  | 完成情况 |文档 |
|-------------|-----------|-----|------|------|
| For         | 循环        |     |      |      |
| variable    | 变量        |     |  完成    |      |
| While       | While变量循环 |     | 完成   |      |
| Switch      | 分流        |     |      |      |
| SQL         | SQL查询     |     | 完成     |      |
| Join        | 关联        |     |      |      |
| Samples     | 采样        |     | 完成   |      |
| Union       | 合并流       |     |      |      |
| SubFlow     | 子流程       |     |      |      |
| Masking     | 数据脱敏      |     | 完成   |      |
| Group       | 数据分组聚合    |     |      |      |
| Checker     | 数据校验      |     |      |      |
| Sort        | 数据排序      |     | 完成   |      |
| AddField    | 新增字段      |     |      |      |
| EditField   | 函数        |     |      |      |
| Mapping     | 字段映射      |     |  完成    |      |
| Rename      | 字段换名      |     | 完成   |      |
| SplitColumn | 列拆分为多行    |     |      |      |
| RowToColumn | 行转列       |     |      |      |
| Str         | 字符串处理     |     |      |      |
| Duplicate   | 去重        |     |      |      |
| Unique      | 唯一行       |     |      |      |
| ColumnToRow | 列转行       |     |      |      |
| Pivot   | 透视        |     |      |      |

#### 专业

| 插件        | 功能     | 类型  | 完成情况 | 文档  |
|-----------|------|-----|------|-----|
| 金融        |     |     |      |     |
| 财务        |     |     |      |     |
| nlp       |     |     |      |     |
| 深度学习      |     |     |      |     |
| 报表展示      |     |     |      |     |
|           |     |     |      |     |



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


### 其他参考

- 项目打包 https://www.cjlmonster.cn/python/setuptools/


### 打包发布命令
 
- 构建源码发布包

```shell
# python setup.py sdist –formats = gztar,zip
# python setup.py bdist_wininst   生成.exe
# python setup.py bdist_rpm       生成.rpm
# python setup.py bdist_egg       生成.egg
# python setup.py bdist           生成多个平台安装包

python setup.py sdist





```

## 使用

```shell
#打包
python setup.py bdist_wheel

#安装
conda activate test_flow

pip install NiceFlow-0.0.1-py3-none-any.whl


```


六、使用setup.py安装包
python setup.py install 将模块安装到全局环境中

python setup.py develop 创建一个软链接指向实际所在目录，不会真正安装

七、如何发布到PyPI
注册PyPI账号，创建~/.pypirc文件，配置PyPI访问地址和账号。

python setup.py register sdist upload -r http://pypi.org 使用该信息注册

python setup.py upload 上传源码包