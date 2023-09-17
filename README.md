## python任务流

### task任务组件功能

- task任务【retry重复执行、delay延迟执行、onSuccess、onError、process、init】
- for循环
- while循环
- if判断
- switch分流
- 串行和并行
- 任务执行【异步执行】和监测

### flow功能
- [x] 增加变量
- flow工作流【flow工作流参数、子流程、暂停、启动】
- 执行引擎【远程执行引擎、本地执行引擎、分布式执行引擎】
- 日志展示
- store任务【mysql、mongo】
- xml、 json加载flow、任务热加载
- 任务管理Rest-API
- 数据增量同步

## 概念学习

- 类型信息     https://www.dusaiphoto.com/article/164/
- 实现插件系统 https://github.com/srn-g/pypluginbase/blob/main/src/PluginManager.py

## 插件

### 输入

| 插件              | 功能             | 类型  | 完成情况     |
|-----------------|----------------|-----|----------|
| Starter         | 启动器          |     |完成       |
| CSVInput        | 读取CSV数据    |     |完成       |
| FakerInput      | 假数据生成      |     |完成       |
| ExcelInput      |                |     |完成        |
| ParquetInput    |                |     |完成          |
| MySQLInput      |                |     |          |
| ESInput         |                |     |          |
| DorisInput      |                |     |          |
| SQLLiteInput    |                |     |          |
| PostgrestInput  |                |     |          |
| HiveInput       |                |     |          |
| PulsarInput     |                |     |          |
| PaimonInput     |                |     |          |
| IceBergInput    |                |     |          |
| ClickHouseInput |                |     |          |
| KafkaInput      |                |     |          |
| MqttInput       |                |     |          |
| OracleInput     |                |     |          |
| SqlserverInput  |                |     |          |
| FlinkCDCInput   |                |     |          |
| MongoInput      |                |     | 完成     |
| DuckDBInput     |                |     |          |
| HttpInput       | Http读          |     |          |
| HtmlInput       | 读取Html中的表格     |     |          |


### 输出

| 插件             | 功能            | 类型   | 完成情况 |
|----------------|---------------|--------|----------|
| ConsoleOutput  | 控制台打印         |        | 完成      |
| HttpWriter     | Http写         |        |          |
| CSVOutput      | CSV输出/切分文件    |      | 完成       |
| HtmlOutput     | 将df写出到html    |      |        |
| MarkdownOutput | 数据写出到markdown |     |   完成       |


### 转换

| 插件         | 功能      | 类型  | 完成情况 |
|------------|---------|-----|------|
| For        | 循环      |     |      |
| While      | While循环 |     | 完成   |
| Switch     | 分流      |     |      |
| SQL        | SQL查询   |     |      |
| Join       | 关联      |     |      |
| Samples    | 采样      |     | 完成   |
| Union      | 合并流     |     |      |
| SubFlow    | 子流程     |     |      |
| Masking    | 数据脱敏    |     | 完成   |
| Group      | 数据分组聚合  |     |      |
| Checker    | 数据校验    |     |      |
| Sort       | 数据排序    |     | 完成   |
| AddField   | 新增字段    |     |      |
| EditField  | 函数      |     |      |
| Mapping    | 字段映射    |     |      |
| Rename     | 字段换名    |     | 完成   |
| SplitColumn | 列拆分为多行  |     |      |
| RowToColumn | 行转列     |     |      |
| Str        | 字符串处理   |     |      |
| Duplicate  | 去重      |     |      |
| Unique     | 唯一行     |     |      |
| ColumnToRow | 列转行     |     |      |

### 专业

| 插件        | 功能     | 类型  | 完成情况 |
|-----------|------|-----|------|
| 金融        |     |     |      |
| 财务        |     |     |      |
| nlp       |     |     |      |
| 深度学习      |     |     |      |
| 报表展示      |     |     |      |
|           |     |     |      |
|           |     |     |      |
|           |     |     |      |

## 分布式

### 角色

- master:分配任务者
- worker:任务执行者
- operator:任务开发者

### 任务执行

- 手动指定任务
- master分配任务

### 定时器工具

## 场景

### 数据清洗

### 数据分析

### 数据管理

### 报表展示

### 大数据数据同步

### 作为工具使用不同数据间转换

- 需要打包发布
-

### 爬虫

## 程序打包发布

## 数据资源

- 可以用来做示例对比 https://github.com/TurboWay/bigdata_analyse
- 地铁人流量数据 https://github.com/geekyouth/SZT-bigdata/blob/master/.file/2018record3.zip

## 二次开发

- 后台管理   https://gitee.com/likeadmin/likeadmin_python?_from=gitee_search
- sql编辑器  https://github.com/pinterest/querybook
- 报表       https://github.com/lightdash/lightdash


