
# AkshareInput 插件文档

___


## 1 快速介绍

借助Akshare库，快速获取采集股票数据，并输出到任意位置
Akshare Github地址：https://github.com/akfamily/akshare
Akshare 文档地址：https://akshare.akfamily.xyz/introduction.html


##  2 pip依赖

pip install akshare


## 3 功能说明

### 3.1 配置样例

```json
{
  "flow": {
    "name": "",
    "uid": "",
    "param": {

    }},
  "nodes": [
    {
      "id": "AKShareInput",
      "name": "read1",
      "type": "input",
      "properties": {
        "api_name":"fund_info_index_em",
        "params": {
          "symbol": "沪深指数",
          "indicator": "增强指数型"
        }
      }
    },
    {
      "id": "CsvOutput",
      "name": "write1",
      "type": "output",
      "properties": {
        "filename": "1.csv"
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
| api_name  | 是    |  | 接口名称 |
| params  | 否    |  | 接口参数 |




