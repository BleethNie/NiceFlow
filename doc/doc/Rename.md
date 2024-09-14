
# Rename 插件文档

___


## 1 快速介绍

修改字段名称


##  2 pip依赖
无


## 3 功能说明

### 3.1 配置样例
```json
{
      "id": "Rename",
      "name": "rename",
      "type": "translate",
      "properties": {
        "columns": [
          {
            "field": "date_id",
            "rename": "new_date_id"
          }
        ],
        "selects": [],
        "excludes": ["content"]
      }
}
```


### 3.2 参数说明

| 参数名称     | 是否必须 | 默认值 | 描述        | 
|----------|------|-----|-----------|
| columns     | 否    | 无   | 需要修改的字段   |
| selects     | 否    | 无   | 需要保留的字段   |
| excludes     | 否    | 无   | 需要drop的字段 |




