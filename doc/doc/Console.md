
# Console 插件文档

___


## 1 快速介绍

控制台打印输出，通常在调试开发时使用。



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

| 参数名称 | 是否必须 | 默认值/示例值 | 描述   | 
|------|------|----|------|
| row  | 否    | 10 | 打印条数 |




