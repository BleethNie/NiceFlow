import unittest

import duckdb
import git
import sqlglot
from sqlglot import select, condition, and_, or_


class TestSQL(unittest.TestCase):

    def test_base(self):
        a = sqlglot.transpile('''

select date_format(RKSJ, '%Y-%m-%d') as dat,SRC, count(*) as coun
from a_rq_real
group by date_format(RKSJ, '%Y-%m-%d'),SRC;
;
''',
                              read="mysql", write="duckdb")[0]
        print(a)


    def test_base_1(self):
        a = sqlglot.transpile('''


SELECT 
    l1.DEVICESRCID,
    TIMESTAMPDIFF(MINUTE, l1.JCCJSJ, l2.JCCJSJ) AS login_interval_minutes
FROM 
    (
        SELECT 
            DEVICESRCID, 
            JCCJSJ,
            ROW_NUMBER() OVER (PARTITION BY DEVICESRCID ORDER BY JCCJSJ) AS rn
        FROM 
            a_rq_real
        WHERE 
            JCCJSJ BETWEEN '2024-07-16' AND '2024-07-16 23:59:59'
    ) l1
INNER JOIN 
    (
        SELECT 
           DEVICESRCID, 
            JCCJSJ,
            ROW_NUMBER() OVER (PARTITION BY DEVICESRCID ORDER BY JCCJSJ) AS rn
        FROM 
            a_rq_real
        WHERE 
            JCCJSJ BETWEEN '2024-07-16' AND '2024-07-16 23:59:59'
    ) l2 ON l1.DEVICESRCID = l2.DEVICESRCID AND l1.rn = l2.rn - 1
WHERE 
    l1.rn = 1 AND l2.rn = 2;



''',
                              read="mysql", write="duckdb")[0]
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
