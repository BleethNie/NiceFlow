# SQL 插件文档

___

## 1 快速介绍

使用sql对数据进行处理

## 2 pip依赖

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
      "id": "CsvInput",
      "name": "read1",
      "type": "input",
      "properties": {
        "filename": "che_test.csv"
      }
    },
    {
      "id": "ExcelInput",
      "name": "read2",
      "type": "input",
      "properties": {
        "filename": "line_data.xlsx"
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
            "table": "s_df"
          },
          {
            "step": "read2",
            "table": "f_df"
          }
        ],
        "sql": "select s_df.*,f_df.line_name from s_df left join f_df on   f_df.line_code =  s_df.line_code ;"
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
    },
    {
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

| 参数名称 | 是否必须 | 默认值/示例值 | 描述         | 
|------|------|----|------------|
| inputs  | 是    |  | 上一步输入节点    |
| sql  | 是    |  | 需要执行的sql语句 |




