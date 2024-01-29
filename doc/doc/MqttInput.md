
# MqttInput 插件文档

___



## 1 快速介绍

从Mqtt Broker中读取数据



## pip依赖

```shell
pip install paho-mqtt


```


## 2 功能说明

### 2.1 配置样例




### 2.2 参数说明

| 参数名称     | 是否必须 | 默认值 | 描述       | 
|------------|------|------|-------------------------------|
| host | 是 | 127.0.0.1 | 数据库地址 |
| port | 是 | 3306 | 数据库端口 |
| db | 是 |  | 数据库名称 |
| username | 是 | root | 数据库用户名 |
| password | 是 | 123456 | 数据库密码 |
| table | 是 |  | 数据库表名 |
| write_method | 是 | insert | 写入方式，支持insert、update、merge、overwrite四种模式 |
| update_keys | 否 |  | 用于update模式的主键，如果为空，则表示不更新 |
| encode_order | 否 |  | 编码顺序，如果为空，则表示不编码 |



