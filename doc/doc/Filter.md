
# Filter 插件文档

___


## 1 快速介绍

数据过滤组件



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

    } },
  "nodes": [
    {
      "id": "FakerInput",
      "name": "read1",
      "type": "input",
      "properties": {
        "rows":10000,
        "columns": ["name","address","city","street_address","date_of_birth","phone_number"],
        "randoms":[
          {"key":"sex","values":["男","女","未知"]}
        ]
      }
    },
    {
      "id": "Filter",
      "name": "filter",
      "type": "output",
      "properties": {
        "condition": "address like '广东%' and sex = '未知' "
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
      "endId": "filter"
    },{
      "startId": "filter",
      "endId": "write1"
    }
  ]
}

```



### 3.2 参数说明

| 参数名称      | 是否必须 | 默认值/示例值 | 描述  | 
|-----------|------|----|-----|
| condition | 是    |  | 过滤 address like '广东%' and sex = '未知' |




