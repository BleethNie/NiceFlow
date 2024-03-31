# SplitFieldToRows 插件文档

___

## 1 快速介绍

一列转多行,将下列2行数据，通过features列分割成5行

| id | features |
|------|------|
|1|    feature1;feature2;feature3|
|2 |    feature4;feature5|

| id | features |new_features|
|------|------|------|
|1    |feature1;feature2;feature3    |feature1|
|1    |feature1;feature2;feature3|    feature2|
|1    |feature1;feature2;feature3    |feature3|
|2    |feature4;feature5    |feature4|
|2    |feature4;feature5|    feature5|

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
      "id": "FakerInput",
      "name": "faker",
      "type": "input",
      "properties": {
        "rows": 10,
        "columns": [
          "name",
          "address",
          "city",
          "street_address",
          "date_of_birth",
          "phone_number"
        ],
        "randoms": [
          {
            "key": "sex",
            "values": [
              "男:1",
              "女:2",
              "未知:3"
            ]
          }
        ]
      }
    },
    {
      "id": "SplitFieldToRowsInput",
      "name": "convert",
      "type": "input",
      "properties": {
        "column": "sex",
        "split": ":",
        "new_column": "new_sex"
      }
    },
    {
      "id": "Console",
      "name": "out",
      "type": "translate",
      "properties": {
        "row": 100
      }
    }
  ],
  "edges": [
    {
      "startId": "faker",
      "endId": "convert"
    },
    {
      "startId": "convert",
      "endId": "out"
    }
  ]
}
```

### 3.2 参数说明

| 参数名称 | 是否必须 | 默认值/示例值 | 描述    | 
|------|------|----|-------|
| column  | 是    |  | 要转换的列 |
| split  | 是    |  | 分隔符 |
| new_column  | 否    |  | 新列名 |




