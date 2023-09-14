## python任务流

- task任务【retry重复执行、delay延迟执行、beforeProcess、afterProcess、onSuccess、onError、process、init】
- flow工作流【flow工作流参数、子流程、暂停、启动】
- 执行引擎【远程执行引擎、本地执行引擎、分布式执行引擎】
- for循环、while循环、if判断、switch、串行和并行
- 日志展示
- store任务【mysql、mongo】
- 任务执行【异步执行】和监测
- xml、json加载flow、任务热加载
- 任务管理Rest-API
- 数据增量同步

## 概念学习

- 类型信息     https://www.dusaiphoto.com/article/164/
- 实现插件系统 https://github.com/srn-g/pypluginbase/blob/main/src/PluginManager.py

## 插件

### 输入

| 插件              | 功能     | 类型  | 完成情况 |
|-----------------|--------|-----|------|
| CSVInput        |        |     |      |
| FakerInput      |        |     |      |
| ExcelInput      |        |     |      |
| ParquetInput    |        |     |      |
| MySQLInput      |        |     |      |
| ESInput         |        |     |      |
| DorisInput      |        |     |      |
| SQLLiteInput    |        |     |      |
| PostgrestInput  |        |     |      |
| HiveInput       |        |     |      |
| PulsarInput     |        |     |      |
| PaimonInput     |        |     |      |
| IceBergInput    |        |     |      |
| ClickHouseInput |        |     |      |
| KafkaInput      |        |     |      |
| MqttInput       |        |     |      |
| OracleInput     |        |     |      |
| SqlserverInput  |        |     |      |
| CdcInput        |        |     |      |
| MongoInput      |        |     |      |
| DuckDBInput     |        |     |      |

### 输出

| 插件              | 功能     | 类型  | 完成情况 |
|-----------------|--------|-----|------|
| ConsoleOutput             | 循环     |     |      |
|           |      |     |      |

### 转换

| 插件          | 功能     | 类型  | 完成情况 |
|-------------|--------|-----|------|
| Starter     | 启动器    |     |      |
| For         | 循环     |     |      |
| Switch      | 分流     |     |      |
| SQL         | SQL查询  |     |      |
| Join        | 关联     |     |      |
| Samples     | 采样     |     |      |
| Union       | 合并流    |     |      |
| SubFlow     | 子流程    |     |      |
| HttpInput   | Http读  |     |      |
| HttpWriter  | Http写  |     |      |
| Masking     | 数据脱敏   |     |      |
| Group       | 数据分组聚合 |     |      |
| Checker     | 数据校验   |     |      |
| Sort        | 数据排序   |     |      |
| Function    | 函数     |     |      |
| Mapping     | 字段映射   |     |      |
| Split       | 列拆分为多行 |     |      |
| RowToColumn | 行转列    |     |      |
| Str         | 字符串处理  |     |      |
| Duplicate   | 去重     |     |      |
| Unique      | 唯一行    |     |      |
| ColumnToRow | 列转行    |     |      |

### 专业

| 插件   | 功能     | 类型  | 完成情况 |
|------|--------|-----|------|
| 金融   |     |     |      |
| 财务   |     |     |      |
| nlp  |     |     |      |
| 深度学习 |     |     |      |
| 报表展示 |     |     |      |
|      |     |     |      |
|      |     |     |      |
|      |     |     |      |
|      |     |     |      |
|      |     |     |      |
|      |     |     |      |
|      |     |     |      |
|      |     |     |      |
|      |     |     |      |

## 分布式

### 角色

- master:分配任务者
- worker:任务执行者
- operator:任务开发者

### 任务执行

- 手动指定任务
- master分配任务

### 定时器工具




