# ExcelInput 插件文档

___

## 1 快速介绍

从excel文件中读取数据

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
      "id": "ExcelInput",
      "name": "read1",
      "type": "input",
      "properties": {
        "filename":"${filename}"
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
      "endId": "write1"
    }
  ]
}

```

### 3.2 参数说明

| 参数名称     | 是否必须 | 默认值/示例值 | 描述                  | 
|----------|------|----|---------------------|
| filename | 是    |  | 需要读取的文件，支持通配符和读取文件夹 |
| sheet_name | 是    |  | sheet名称             |
