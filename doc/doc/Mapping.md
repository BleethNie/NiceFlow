# Mapping 插件文档

___

## 1 快速介绍

字段映射组件,支持2种模式 value_mapping=自己设置值 plugin_mapping=从其它组件映射

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
      "common": "E:\\02_Resource\\01_Code\\python\\NiceFlow\\NiceFlow\\doc"
    }
  },
  "nodes": [
    {
      "id": "FakerInput",
      "name": "read1",
      "type": "input",
      "properties": {
        "rows": 1000,
        "columns": [
          "phone_number"
        ],
        "randoms": [
          {
            "key": "sex1",
            "values": [
              "男",
              "女",
              "未知"
            ]
          },
          {
            "key": "sex2",
            "values": [
              "男",
              "女",
              "未知"
            ]
          }
        ]
      }
    },
    {
      "id": "ExcelInput",
      "name": "dict1",
      "type": "input",
      "properties": {
        "file_name": "${common}\\excel格式字典.xlsx",
        "sheet_name": "性别"
      }
    },
    {
      "id": "Mapping",
      "name": "mapping",
      "type": "translate",
      "properties": {
        "columns": [
          {
            "field": "sex1",
            "default": "NONE",
            "mapping_field": "sex1",
            "value_mapping": {
              "男": "1",
              "女": "2"
            }
          },
          {
            "field": "sex2",
            "mapping_field": "sex21",
            "plugin_mapping": {
              "step_name": "dict1",
              "key_field": "性别key",
              "value_field": "字典值"
            }
          }
        ]
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
      "endId": "mapping"
    },
    {
      "startId": "dict1",
      "endId": "mapping"
    },
    {
      "startId": "mapping",
      "endId": "print"
    }
  ]
}

```

### 3.2 参数说明

| 参数名称      | 是否必须 | 默认值/示例值 | 描述     | 
|-----------|------|----|--------|
| columns | 是    |  | 需要映射的列 |

```json5
{
  "field": "sex1",          //需要映射的列 
  "default": "NONE",        //默认值
  "mapping_field": "sex1",  //映射后列名称，如果和原列同名，则进行替换，空值则表示替换
  "value_mapping": {        //需要映射的值
    "男": "1",
    "女": "2"
  }
}

```

```json5
{
  "field": "sex2",             //需要映射的列
  "mapping_field": "sex21",    //映射后列名称，如果和原列同名，则进行替换，空值则表示替换
  "plugin_mapping": {          //使用插件映射，从step_name指定的组件中获取数据，key_field为key，value_field为value
    "step_name": "dict1",
    "key_field": "性别key",
    "value_field": "字典值"
  }
}

```


