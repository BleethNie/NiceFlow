
# FrameInput 插件文档

___


## 1 快速介绍

从duckdb的dataframe中获取数据，需要在代码中使用

##  2 pip依赖



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
      "id": "FrameInput",
      "name": "frame",
      "type": "input",
      "properties": {
        "frame_name":"frame_input"
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
      "startId": "frame",
      "endId": "out"
    }
  ]
}

```

### 3.2 python代码示例1


```python
import unittest
import pandas as pd
import duckdb
from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestFrameInput(unittest.TestCase):

    # 从其它流程结果中获取frame
    def test_frame_input_1(self):
        path = "faker_input.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()
        result_dict = myFlow.get_result()
        duck_df = list(result_dict.values())[0]

        # 从其它地方获取的数据，设置到流程中
        path = "frame_input.json"
        myFlow2: Flow = FlowManager.read(path)
        myFlow2.set_result("frame_input",duck_df)
        myFlow2.run()

    # 从pandas dataframe中获取结果
    def test_frame_input_2(self):
        path = "frame_input.json"
        df = pd.read_csv("che_test_2.csv")
        duck_df2 = duckdb.from_df(df)
        myFlow3: Flow = FlowManager.read(path)
        myFlow3.set_result("frame_input",duck_df2)
        myFlow3.run()

```

### 3.2 python代码示例2





### 3.2 参数说明

| 参数名称     | 是否必须 | 默认值/示例值 | 描述         | 
|----------|------|----|------------|
| frame_name     | 是    |  | 需要读取的frame |




