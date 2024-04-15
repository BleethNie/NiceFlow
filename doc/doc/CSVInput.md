# CsvInput 插件文档

___

## 1 快速介绍

从csv文件中读取数据,参数配置可以参考duckdb的read_csv函数，https://duckdb.org/docs/data/csv/overview.html

## 3 功能说明

### 3.1 配置样例

* 配置一个从csv文件同步抽取数据到本地的作业:

```
{
  "flow": {
    "name": "",
    "uid": "",
    "param": {

    }},
  "nodes": [
    {
      "id": "CsvInput",
      "name": "read1",
      "type": "input",
      "properties": {
        "filename": "F:\\07_数据源大全\\store_order\\sales.csv"
      }
    },
    {
      "id": "CsvInput",
      "name": "read2",
      "type": "input",
      "properties": {
        "filename": "F:\\07_数据源大全\\store_order\\store.csv"
      }
    },
    {
      "id": "SQL",
      "name": "sql",
      "type": "translate",
      "properties": {
        "inputs": [
          {
            "step": "read1",
            "table": "sales_df"
          },
          { 
            "step": "read2",
            "table": "store_df"
          }
        ],
        "sql": "select store_df.store_pk,sales_df.date_id as ddd from sales_df left join  store_df  on sales_df.store_id = sales_df.store_id limit 10"
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
      "endId": "sql"
    },{
      "startId": "read2",
      "endId": "sql"
    },
    {
      "startId": "sql",
      "endId": "write1"
    }
  ]
}
```

### 3.2 参数说明

| 参数名称     | 是否必须 | 默认值/示例值 | 描述                                                             | 
|----------|------|----|----------------------------------------------------------------|
| filename | 是    |  | 需要读取的文件，支持通配符和读取文件夹                                            |
| 其它参数     |     |  | 其它参数都是非必填参数， 参考：https://duckdb.org/docs/data/csv/overview.html |
