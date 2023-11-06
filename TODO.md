## NiceFlow

> 类似Kettle工具，主要实现数据ETL处理

### 未来功能

#### 插件基类
- onSuccess 功能
- onError 功能
- 插件字段、字段注释功能
- 自动建表功能
- batch处理和stream处理
- savepoint功能


#### 插件开发
- IF组件-变量，选择不同分支
A->IF->B/C

- For组件-值/变量,循环执行分支
A->For->B[获取一行记录]->执行一个子流程->B[是否执行完成]->C[执行另外一个分支]

- While组件-变量，
- Switch组件-值/变量，切换不同分支
- Join组件，多个数据进行合并
- mapping组件，字典映射
- 

#### Edge属性开发
- edge 类型设置 

```
"properties":{
  "type": "copy/condition[True/False]/Execution[SUCCESS/ERROR]"
}
```

#### cli
- 数据探索
- [x] 支持数据源配置加密/解密
- 支持定时执行任务
- YouPlot

#### core
- 系统变量支持【全局变量、Flow变量】
1.上一步行数
2.时间变量
3.[参考](https://dolphinscheduler.apache.org/zh-cn/docs/3.2.0/guide/project/workflow-instance)

- 支持HTTP、HDFS、COS、S3直接访问数据库
- 支持Git读取任务【动态读取任务】
- 支持数据源配置加密
- 插件执行异常通知【飞书、钉钉、邮件、HTTP】
- 支持代码中编写任务
- 支持日志入数据库
- 支持日志写到web页面
- 支持不用格式任务【xml,json,yaml】

#### 集群
- 开发集群模式


#### 测试


#### DEMO案例








