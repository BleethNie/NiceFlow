
# JsonInput 插件文档

___


## 1 快速介绍

写入json文件插件,借助pandas实现 `pd.to_json(filename)`


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
          { "key": "sex", "values": [  "男", "女", "未知" ] },
          { "key": "zt", "values": [  "已婚", "未婚", "未知" ] }
        ]
      }
    },
    {
      "id": "Duplicate",
      "name": "duplicate",
      "type": "input",
      "properties": {
        "duplicate_fields": ["sex","zt"],
        "order_fields": "name",
        "order_type": "DESC"
      }
    },
    {
      "id": "JsonOutput",
      "name": "write1",
      "type": "output",
      "properties": {
        "filename": "1.json",
        "indent": 4
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

| 参数名称     | 是否必须 | 默认值/示例值 | 描述                   | 
|----------|------|----|----------------------|
| filename | 是    |  | 文件名                  |
| -        | 否    |  | 其它参数参考pandas to_json |




