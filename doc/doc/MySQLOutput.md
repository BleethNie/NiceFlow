
# MySQLOutput 插件文档

___

## 1 快速介绍

将数据写入到mysql数据库中，写入方式支持insert、update、merge、overwrite四种模式
- 写入实际的表中,表不存在则自动创建
- insert/只插入数据[无主键则全部插入，有主键则根据主键判断是否插入]
- update/只更新数据[需要更新键]
- overwrite/清空数据并导入[不需要数据]
- merge/根据主键判断是更新或者插入[必须有主键]

## pip依赖

```shell
pip install pymysql

pip install sqlalchemy

```

## 2 功能说明

### 2.1 配置样例

* 配置一个从csv文件同步抽取数据到本地的作业:

```

```




### 2.2 参数说明

| 参数名称     | 是否必须 | 默认值 | 描述       | 
|------------|------|------|-------------------------------|
| host | 是 | 127.0.0.1 | 数据库地址 |
| port | 是 | 3306 | 数据库端口 |
| db | 是 |  | 数据库名称 |
| user | 是 | root | 数据库用户名 |
| password | 是 | 123456 | 数据库密码 |
| table | 是 |  | 数据库表名 |
| write_method | 是 | insert | 写入方式，支持insert、update、merge、overwrite四种模式 |
| update_keys | 否 |  | 用于update模式的主键，如果为空，则表示不更新 |
| encode_order | 否 |  | 编码顺序，如果为空，则表示不编码 |

### 性能测试

#### insert

#### update

#### merge

#### overwrite
