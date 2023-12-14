
# CsvInput 插件文档

___



## 1 快速介绍

从csv文件中读取数据，并将数据写入到对应的数据库表中。



## 2 功能说明

### 2.1 配置样例

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
        "file_name": "F:\\07_数据源大全\\store_order\\sales.csv"
      }
    },
    {
      "id": "CsvInput",
      "name": "read2",
      "type": "input",
      "properties": {
        "file_name": "F:\\07_数据源大全\\store_order\\store.csv"
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




### 2.2 参数说明

* **file_name**

    * 描述：csv文件名 支持文件夹 如：'folder/*.csv' 

    * 必选：是 <br />

    * 默认值：无 <br />

* **header**

    * 描述：boolean类型，是否包含表头,true为包含，false为不包含。

    * 必选：否 <br />

    * 默认值：无 <br />

