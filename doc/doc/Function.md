
# Function 插件文档

___


## 1 快速介绍

自定义函数(udf)插件,自定义函数参考：https://duckdb.org/docs/api/python/function,目前未看到udaf,udtf实现方式


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
        "rows":100,
        "columns": ["name","address","city","street_address","date_of_birth","phone_number"],
        "randoms":[
          {"key":"sex","values":["男","女","未知"]}
        ]
      }
    },
    {
      "id": "Function",
      "name": "f",
      "type": "output",
      "properties": {
        "function_paths": [
          "E:\\02_Resource\\01_Code\\python\\NiceFlow\\NiceFlow\\samples\\function\\a_function.py"
        ],
        "columns": [
          {"key": "sex", "function": "print_a(sex)"}
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
      "endId": "f"
    },{
      "startId": "f",
      "endId": "write1"
    }
  ]
}

```



### 3.2 参数说明

| 参数名称      | 是否必须 | 默认值/示例值 | 描述                                                                               | 
|-----------|------|----|----------------------------------------------------------------------------------|
| function_paths | 否    |  | 用户自定义函数路径,(NiceFlow本身有系统自定义函数，位于src/NiceFlow/core/functions.py文件中,系统自定义函数可以直接使用) |
| columns | 是    |  | 需要函数转换的列                                                                         |




