import unittest

import duckdb
import git
import sqlglot
from sqlglot import select, condition, and_, or_


class TestSQL(unittest.TestCase):

    def test_base(self):
        a = sqlglot.transpile('''
      CREATE TABLE `cde_dictionary` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键',
  `type` varchar(50) NOT NULL COMMENT '字典分类',
  `description` varchar(200) NOT NULL COMMENT '字典描述',
  `code` varchar(50) NOT NULL COMMENT '字典编码',
  `value` varchar(100) NOT NULL COMMENT '字典值',
  `is_deleted` tinyint(1) NOT NULL COMMENT '是否逻辑删除',
  `created_ts` datetime NOT NULL COMMENT '创建时间',
  `updated_ts` datetime NOT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_type_code` (`type`,`code`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='字典表';''',
                              read="mysql", write="doris")[0]
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
