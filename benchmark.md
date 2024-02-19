
##
1. 硬件环境
   机器数量	4 台腾讯云主机（1个FE，3个BE）
   CPU	AMD EPYC™ Milan(2.55GHz/3.5GHz) 16核
   内存	64G
   网络带宽	7Gbps
   磁盘	高性能云硬盘


2. 软件环境
   Doris 部署 3BE 1FE；
   内核版本：Linux version 5.4.0-96-generic (buildd@lgw01-amd64-051)
   操作系统版本：Ubuntu Server 20.04 LTS 64位
   Doris 软件版本： Apache Doris 1.2.0-rc01、Apache Doris 1.1.3 及 Apache Doris 0.15.0 RC04
   JDK：openjdk version "11.0.14" 2022-01-18


3. 测试数据量
   SSB表名	行数	备注
   lineorder	600,037,902	商品订单明细表表
   customer	3,000,000	客户信息表
   part	1,400,000	零件信息表
   supplier	200,000	供应商信息表
   dates	2,556	日期表
   lineorder_flat	600,037,902	数据展平后的宽表

5. 标准 SSB 测试结果
   这里我们使用 Apache Doris 1.2.0-rc01、Apache Doris 1.1.3 及 Apache Doris 0.15.0 RC04 版本进行对比测试，测试结果如下：

Query	Apache Doris 1.2.0-rc01(ms)	Apache Doris 1.1.3 (ms)	Apache Doris 0.15.0 RC04(ms)
Q1.1	40	18	350
Q1.2	30	100	80
Q1.3	20	70	80
Q2.1	350	940	20680
Q2.2	320	750	18250
Q2.3	300	720	14760
Q3.1	650	2150	22190
Q3.2	260	510	8360
Q3.3	220	450	6200
Q3.4	60	70	160
Q4.1	840	1480	24320
Q4.2	460	560	6310
Q4.3	610	660	10170
合计	4160	8478	131910
结果说明

测试结果对应的数据集为scale 100, 约6亿条。
测试环境配置为用户常用配置，云服务器4台，16核 64G SSD，1 FE 3 BE 部署。
选用用户常见配置测试以降低用户选型评估成本，但整个测试过程中不会消耗如此多的硬件资源。

customercsv 56663 KB
dates.csv 228 KB
lineorder.csv 11,747,02...
part.csv 85,101 KB
supplier.csv 3.345 KB







```sql
CREATE TABLE IF NOT EXISTS lineorder (
  lo_orderkey INTEGER ,
  lo_linenumber INTEGER  ,
  lo_custkey INTEGER ,
  lo_partkey INTEGER ,
  lo_suppkey INTEGER ,
  lo_orderdate INTEGER ,
  lo_orderpriority VARCHAR ,
  lo_shippriority INTEGER ,
  lo_quantity INTEGER ,
  lo_extendedprice INTEGER ,
  lo_ordtotalprice INTEGER ,
  lo_discount INTEGER ,
  lo_revenue INTEGER ,
  lo_supplycost INTEGER ,
  lo_tax INTEGER ,
  lo_commitdate INTEGER ,
  lo_shipmode VARCHAR 
) ;

CREATE TABLE IF NOT EXISTS customer (
  c_custkey INTEGER ,
  c_name varchar ,
  c_address varchar ,
  c_city varchar ,
  c_nation varchar ,
  c_region varchar ,
  c_phone varchar ,
  c_mktsegment varchar 
);

CREATE TABLE IF NOT EXISTS dates (
  d_datekey INTEGER ,
  d_date varchar ,
  d_dayofweek varchar ,
  d_month varchar ,
  d_year INTEGER ,
  d_yearmonthnum INTEGER ,
  d_yearmonth varchar ,
  d_daynuminweek INTEGER ,
  d_daynuminmonth INTEGER ,
  d_daynuminyear INTEGER ,
  d_monthnuminyear INTEGER ,
  d_weeknuminyear INTEGER ,
  d_sellingseason varchar ,
  d_lastdayinweekfl INTEGER ,
  d_lastdayinmonthfl INTEGER ,
  d_holidayfl INTEGER ,
  d_weekdayfl INTEGER 
) ;

 CREATE TABLE IF NOT EXISTS supplier (
  s_suppkey INTEGER ,
  s_name varchar ,
  s_address varchar ,
  s_city varchar ,
  s_nation varchar ,
  s_region varchar ,
  s_phone varchar 
);

CREATE TABLE IF NOT EXISTS part (
  p_partkey INTEGER ,
  p_name varchar ,
  p_mfgr varchar ,
  p_category varchar ,
  p_brand varchar ,
  p_color varchar ,
  p_type varchar ,
  p_size INTEGER ,
  p_container varchar 
) ;
```


```
--20s
COPY lineorder FROM 'F:/07_数据源大全/ssb-dbgen/data/lineorder.csv' (DELIMITER '|');

--49ms
COPY supplier FROM 'F:/07_数据源大全/ssb-dbgen/data/supplier.csv' (DELIMITER '|');


--1.158s
COPY part FROM 'F:/07_数据源大全/ssb-dbgen/data/part.csv' (DELIMITER '|');

--863ms
COPY customer FROM 'F:/07_数据源大全/ssb-dbgen/data/customer.csv' (DELIMITER '|');

--21ms
COPY dates FROM 'F:/07_数据源大全/ssb-dbgen/data/dates.csv' (DELIMITER '|');
```


```
select 'part' as tb, count(*) from part union all
select 'customer' as tb, count(*) from customer union all
select 'supplier' as tb, count(*) from supplier union all
select 'dates' as tb, count(*) from dates union all
select 'lineorder' as tb, count(*) from lineorder;


part	1000000
customer	600000
supplier	40000
dates	2556
lineorder	119994608

```


CALL pragma_database_size();
1	3.8GB	262144	14852	14843	9	242KB	2.9GB	53.6GB


