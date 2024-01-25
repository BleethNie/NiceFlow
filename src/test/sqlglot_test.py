import unittest

import duckdb
import git
import sqlglot
from sqlglot import select, condition, and_, or_


class TestSQL(unittest.TestCase):

    def test_base(self):
        a = sqlglot.transpile('''
       CREATE TABLE `rq_real` (
  `ID` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `JCZ` double NOT NULL COMMENT '检测值',
  `JCZB` varchar(32) NOT NULL COMMENT '检测指标',
  `BZ` varchar(255) NOT NULL COMMENT '备注',
  `DEVICESRCID` varchar(32) NOT NULL COMMENT '设备原标识码',
  `DWBSM` varchar(32) NOT NULL COMMENT '点位标识码',
  `JCCJSJ` datetime NOT NULL COMMENT '采集时间',
  `JCSBSJ` datetime NOT NULL COMMENT '上报时间',
  `RKSJ` datetime NOT NULL COMMENT '入库时间',
  `SBBSM` varchar(32) NOT NULL COMMENT '设备标识码',
  `SRC` varchar(32) DEFAULT NULL COMMENT '数据来源'

) ENGINE=InnoDB AUTO_INCREMENT=51796845 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC COMMENT='燃气实时数据'
''',
                              read="mysql", write="hive")[0]
        print(a)

    def test_base_1(self):
        a = sqlglot.transpile('''from a;''',
                              read="duckdb", write="mysql")[0]
        print(a)

    def test_build_sql(self):
        where = condition("x=1").and_("y=1")
        sql = select("*").from_("y").where(where).sql()
        print(sql)

    def test_build_sql_1(self):
        where = or_("b=1", and_("y=1", "z=1"))
        print(where)
        sql = select("*").from_("y").where(where).sql(dialect="duckdb")
        print(sql)


if __name__ == '__main__':
    unittest.main()
