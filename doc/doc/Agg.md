
# Agg 插件文档

___


## 1 快速介绍

使用DuckDB的聚合函数，完成相关数据聚合操作


##  2 pip依赖



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
      "id": "FakerInput",
      "name": "read1",
      "type": "input",
      "properties": {
        "rows": 10000,
        "columns": [
          "name",
          "address",
          "city",
          "street_address",
          "date_of_birth",
          "phone_number"
        ],
        "randoms": [
          {
            "key": "sex",
            "values": [
              "男",
              "女",
              "未知"
            ]
          }
        ]
      }
    },
    {
      "id": "Console",
      "name": "print1",
      "type": "output",
      "properties": {
        "row": 1000
      }
    },
    {
      "id": "Agg",
      "name": "agg",
      "type": "output",
      "properties": {
        "keys": ["name"],
        "aggs": [
          {
            "value": "sex",
            "agg": "group_concat"
          },
          {
            "value": "date_of_birth",
            "agg": "count"
          }
        ]
      }
    },
    {
      "id": "Console",
      "name": "print2",
      "type": "output",
      "properties": {
        "row": 1000
      }
    }
  ],
  "edges": [
    {
      "startId": "read1",
      "endId": "print1"
    },
    {
      "startId": "print1",
      "endId": "agg"
    },
    {
      "startId": "agg",
      "endId": "print2"
    }
  ]
}

```



### 3.2 参数说明

| 参数名称 | 是否必须 | 默认值/示例值 | 描述         | 
|------|------|----|------------|
| keys  | 是    |  | 分组字段,Array |
| aggs  | 是    |  | 聚合字段,Array        |




