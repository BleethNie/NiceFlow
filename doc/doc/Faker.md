
# Faker 插件文档

___


## 1 快速介绍

假数据生成器,使用Faker库生成假数据，https://github.com/joke2k/faker



##  2 pip依赖

pip install Faker



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
      "endId": "write1"
    }
  ]
}

```



### 3.2 参数说明

| 参数名称 | 是否必须 | 默认值/示例值 | 描述                                  | 
|------|------|----|-------------------------------------|
| rows  | 是    | 10 | 数据生成行数                              |
| columns  | 是    | ["name","address","city","street_address","date_of_birth","phone_number"] | 生成列,例如：name列实际为`fake.name()`值,其它列类似 |
| randoms  | 否    | [] | 随机列，key为列名，values为随机值列表 |                            |




