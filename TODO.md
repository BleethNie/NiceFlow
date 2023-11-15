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

- 支持HTTP、HDFS、COS、S3直接访问数据源
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


#### 问题

- 如何实现增量更新，哪种方式比较高效，不会出错
- 如何实现数据同步，同步过程中不出现问题【多数据，少数据】
- -- 同步完成后查询两端数据量是否一致
- -- 
- 数据监控如何实现，能够监控数据层面的问题
- -- 任务是否停止告警
- 如何实现报表展示
- 


#### 辅助命令【基本信息探查】

- 查询hive文件大小/文件数目

```shell
dbs=$(hadoop fs -ls /user/hive/warehouse | awk '{print $8}')

for db in $dbs
do
echo "统计库：$db"
tables=$(hadoop fs -ls "$db" | awk '{print $8}')
for table in $tables
do
echo "统计表：$table"
size=$(hadoop fs -count -h "$table" | awk '{print $3}')
echo "表 $table 占用空间为：$size"
echo "$table,$size" >> result.csv
done
done

```

- maxcompute 表大小/文件数目/count数目
- 表分区信息
- 表元数据信息
- 表创建时间/修改时间/更新时间

- mysql 数据库表数目/数量/每天新增数量



