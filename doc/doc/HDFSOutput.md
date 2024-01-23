
# HDFSOutput 插件文档

___


## 1 快速介绍

将数据写入hdfs的插件。

***注意事项***:运行程序的主机需要增加host配置，如hadoop服务器host为 `192.168.1.90  bigdata-90`,需要将该信息配置到运行主机上

## 2.需要安装的依赖包

```shell

pip install hdfs

```


## 3 功能说明

### 3.1 配置样例

* 配置一个将数据写入hdfs的作业:

```
{
  "flow": {
    "name": "",
    "uid": "",
    "param": {

    }},
  "nodes": [
    {
      "id": "MySQLInput",
      "name": "read1",
      "type": "input",
      "properties": {
        "host": "127.0.0.1",
        "port": 3306,
        "username": "root",
        "password": "123456",
        "query": "select * from che.cde_config;"
      }
    },{
      "id": "HDFSOutput",
      "name": "out",
      "type": "translate",
      "properties": {
        "url": "http://192.168.1.90:9870", --ipc port
        "user": "hdfs",   
        "source": "config.csv",
        "dest": "/tmp/config.csv",
        "partitions": "",
        "columns": "",
        "format": "csv,parque"
      }
    }
  ],
  "edges": [
    {
      "startId": "read1",
      "endId": "out"
    }
  ]
}
```



### 3.2 参数说明

* **url**
    * 描述：
    * 必选：是 <br />
    * 默认值：无 <br />

* **user**
  * 描述：
  * 必选：是 <br />
  * 默认值：无 <br />


* **source**
  * 描述：
  * 必选：是 <br />
  * 默认值：无 <br />


* **dest**
  * 描述：
  * 必选：是 <br />
  * 默认值：无 <br />


* **partitions**
  * 描述：
  * 必选：是 <br />
  * 默认值：无 <br />


* **format**
  * 描述：
  * 必选：是 <br />
  * 默认值：无 <br />

* **columns**
  * 描述：
  * 必选：是 <br />
  * 默认值：无 <br />


