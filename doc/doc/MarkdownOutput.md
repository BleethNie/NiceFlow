
# MarkdownOutput 插件文档

___


## 1 快速介绍

将数据写出为markdown格式文件,基于pandas `pd.to_markdown()`


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
      "id": "Rename",
      "name": "rename",
      "type": "translate",
      "properties": {
        "columns": [
          {
            "field": "date_id",
            "rename": "date_id_id"
          }
        ]
      }
    },
    {
      "id": "MarkdownOutput",
      "name": "print",
      "type": "output",
      "properties": {
        "filename": "a.md",
        "encoding": "gbk"
      }
    }
  ],
  "edges": [
    {
      "startId": "read1",
      "endId": "rename"
    },
    {
      "startId": "rename",
      "endId": "print"
    }
  ]
}

```



### 3.2 参数说明

| 参数名称     | 是否必须 | 默认值/示例值 | 描述   | 
|----------|------|----|------|
| filename | 是    |  | 文件名  |
| encoding | 否    |  utf-8| 编码   |
| limit | 否    |  | 限制行数 |

