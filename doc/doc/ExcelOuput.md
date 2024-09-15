# ExcelOutput 插件文档

___

## 1 快速介绍

写入数据到excel文件中

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
        "file_name":"${file_name}"
      }
    },
    {
      "id": "ExcelOutput",
      "name": "write1",
      "type": "output",
      "properties": {
        "file_name": "${out_name}"
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
