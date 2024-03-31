
# MqttInput 插件文档

___


## 1 快速介绍

订阅Mqtt Broker topic中的数据,流式处理数据



##  2 pip依赖

```shell
pip install paho-mqtt

```


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
      "id": "MqttInput",
      "name": "read1",
      "type": "input",
      "properties": {
        "host": "192.168.1.90",
        "port": 1883,
        "topic": "/a/a",
        "username": "",
        "password": ""
      }
    },
    {
      "id": "MySQLOutput",
      "name": "out",
      "type": "translate",
      "properties": {
        "host": "127.0.0.1",
        "port": 3306,
        "username": "root",
        "password": "123456",
        "db": "che",
        "table": "che_config",
        "write_method": "insert"
      }
    }
  ],
  "edges": [
    {
      "startId": "read1",
      "endId": "out"
    }
  ]
}

```



### 3.2 参数说明

| 参数名称     | 是否必须 | 默认值       | 描述      | 
|----------|------|-----------|---------|
| host     | 是    | 127.0.0.1 | 数据库地址   |
| port     | 否    | 1883      | 默认为1883 |
| username | 否    | root      | 用户名     |
| password | 否    | 123456    | 密码      |
| topic    | 是    | /a/a      | 订阅主题    |
| client_id | 否    |     | 客户端ID   |




