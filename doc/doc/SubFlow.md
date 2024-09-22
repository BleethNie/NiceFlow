
# SubFlow 插件文档

___


## 1 快速介绍

子流程插件，用于实现子流程的调用，子流程的配置与主流程一致



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
      "id": "HttpInput",
      "name": "read1",
      "type": "input",
      "properties": {
        "port": 8080,
        "handler_url": "/data"
      }
    },
    {
      "id": "SubFlow",
      "name": "subflow",
      "type": "translate",
      "properties": {
        "flow": "E:\\02_Resource\\01_Code\\python\\NiceFlow\\doc\\sort_console.json"
      }
    },
    {
      "id": "Console",
      "name": "print",
      "type": "output",
      "properties": {
        "row": 10
      }
    }
  ],
  "edges": [
    {
      "startId": "read1",
      "endId": "subflow"
    },
    {
      "startId": "subflow",
      "endId": "print"
    }
  ]
}

```



### 3.2 参数说明

| 参数名称      | 是否必须 | 默认值/示例值 | 描述  | 
|-----------|------|----|-----|
| condition | 是    |  | 过滤 address like '广东%' and sex = '未知' |




