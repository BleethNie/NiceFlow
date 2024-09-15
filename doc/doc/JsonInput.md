
# JsonInput 插件文档

___


## 1 快速介绍

json文件读取组件,需要duckdb 扩展支持

```shell
INSTALL json;
LOAD json;

```
duckdb参考：

- https://duckdb.org/docs/extensions/json
- https://duckdb.org/docs/data/json/overview

##  2 pip依赖

无


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
      "id": "JsonInput",
      "name": "read1",
      "type": "input",
      "properties": {
        "filename": "F:\\12_新闻数据集\\1623-0000001\\zh\\part-663de978334d-000000.jsonl",
        "format": "newline_delimited"
      }
    },
    {
      "id": "Console",
      "name": "c1",
      "type": "output",
      "properties": {
        "row": 100
      }
    },
    {
      "id": "Rename",
      "name": "rename",
      "type": "translate",
      "properties": {
        "columns": [
          {
            "field": "date",
            "rename": "publish_date"
          }
        ]
      }
    },
    {
      "id": "Console",
      "name": "c2",
      "type": "output",
      "properties": {
        "row": 100
      }
    }

  ],
  "edges": [
    {
      "startId": "read1",
      "endId": "c1"
    },  {
      "startId": "c1",
      "endId": "rename"
    },
    {
      "startId": "rename",
      "endId": "c2"
    }
  ]
}

```



### 3.2 参数说明

| 参数名称      | 是否必须 | 默认值/示例值 | 描述                                   | 
|-----------|------|----|--------------------------------------|
| filename | 是    |  | 文件名，支持通配符 *                          |
| format | 否    |  |  | 文件格式




