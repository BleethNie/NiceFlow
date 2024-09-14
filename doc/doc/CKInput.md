
# CKInput 插件文档

___


## 1 快速介绍

ClickHouse的输入插件，支持从ClickHouse读取数据。

##  2 pip依赖

pip install clickhouse-driver

## 3 功能说明

### 3.1 配置样例

```json
{
  "flow": {
    "name": "",
    "uid": "",
    "param": {
    }
  },
  "nodes": [
    {
      "id": "CKInput",
      "name": "read1",
      "type": "input",
      "properties": {
        "host": "192.168.1.90",
        "port": 9000,
        "db": "default",
        "table": "station",
        "sql": "select * from station limit 100000"
      }
    },
    {
      "id": "CKOutput",
      "name": "print",
      "type": "output",
      "properties": {
        "host": "192.168.1.90",
        "port": 9000,
        "db": "default",
        "table": "new_station"
      }
    }
  ],
  "edges": [
    {
      "startId": "read1",
      "endId": "print"
    }
  ]
}

```



### 3.2 参数说明

| 参数名称     | 是否必须 | 默认值/示例值 | 描述      | 
|----------|------|----|---------|
| host     | 是    |  | 数据库地址   |
| port     | 是    |  | 数据库端口   |
| db       | 是    |  | 数据库名称   |
| username | 是    |  | 用户名     |
| password | 是    |  | 密码      |
| table    | 否    |  | 表名称     |
| sql      | 否    |  | 查询sql语句 |




