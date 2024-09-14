# Console 插件文档

___

## 1 快速介绍

数据去重组件

## 2 pip依赖

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
          },
          {
            "key": "zt",
            "values": [
              "已婚",
              "未婚",
              "未知"
            ]
          }
        ]
      }
    },
    {
      "id": "Duplicate",
      "name": "duplicate",
      "type": "input",
      "properties": {
        "duplicate_fields": [
          "sex",
          "zt"
        ],
        "order_fields": "name",
        "order_type": "DESC"
      }
    },
    {
      "id": "Console",
      "name": "write1",
      "type": "output",
      "properties": {
        "row": 100
      }
    }
  ],
  "edges": [
    {
      "startId": "read1",
      "endId": "duplicate"
    },
    {
      "startId": "duplicate",
      "endId": "write1"
    }
  ]
}

```

### 3.2 参数说明

| 参数名称 | 是否必须 | 默认值/示例值 | 描述                      | 
|------|------|----|-------------------------|
| duplicate_fields | 是    |  | 需要去重的字段，可以为多个字段         |
| order_fields | 是    |  | 排序字段                    |
| order_type | 是    |  | 排序类型，默认为升序，可选值：DESC、ASC |




