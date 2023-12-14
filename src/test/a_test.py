import calendar
import datetime
from datetime import datetime as dt
import unittest
# 导入 re 模块，用来进行正则表达式匹配
import re

# 定义一个字符串，包含多个 ${cde_config} 包裹的变量
s = "Hello, ${row.name}. Your age is ${row_age}. Your favorite color is ${color}."

# 定义一个 dict，用来存储变量的值
d = {"row.name": "AAAA", "row_age": 25, "color": "red"}



# 获取第一天和最后一天
def getEndDay(row):
    c_yearmonth = str(row["c_yearmonth"])
    year = int(c_yearmonth[0:4])
    month = int(c_yearmonth[4:6])
    firstDay = datetime.date(year,month,day=1)

    d_date = str(row["d_date"])
    d_date_d = dt.strptime(d_date, '%Y-%m-%d %H:%M:%S')

    offset = datetime.timedelta(days=d_date_d.day-1)
    re_date_str = (firstDay + offset).strftime('%Y-%m-%d %H:%M:%S')
    # 返回第一天和最后一天
    re_date = dt.strptime(re_date_str ,'%Y-%m-%d %H:%M:%S')
    if "2024-03-29"== re_date_str[0:10]:
        print(re_date_str)
        previous_month_date = re_date.replace(month=re_date.month-1,day=re_date.day-1)
    elif "2024-03-30" == re_date_str[0:10]:
        print(re_date_str)
        previous_month_date = re_date.replace(month=re_date.month-1,day=re_date.day-2)
    elif "2024-03-31" == re_date_str[0:10]:
        print(re_date_str)
        previous_month_date = re_date.replace(month=re_date.month-1,day=re_date.day-3)
    elif re_date_str[0:10] in ["2023-12-31","2024-05-31","2024-07-31","2024-10-31","2024-12-31"]:
        print(re_date_str)
        previous_month_date = re_date.replace(month=re_date.month-1,day=re_date.day-1)
    else:
        if re_date_str[0:8] == "2024-01-":
            previous_month_date = re_date.replace(month=re_date.month+11)
        else:
            previous_month_date = re_date.replace(month=re_date.month-1)
    return previous_month_date.strftime('%Y-%m-%d %H:%M:%S')


# 获取第一天和最后一天
def date_format(row):
    dd = row["d_date"]
    return dd.strftime('%Y-%m-%d %H:%M:%S')

# 获取第一天和最后一天
def getFirstDay(row):
    c_yearmonth = str(row["c_yearmonth"])
    year = int(c_yearmonth[0:4])
    month = int(c_yearmonth[4:6])
    # 获取当前月的第一天的星期和当月总天数
    weekDay,monthCountDay = calendar.monthrange(year,month)
    # 获取当前月份第一天
    firstDay = datetime.date(year,month,day=1)
    offset = datetime.timedelta(days=-1)
    day = dt.strptime(str(firstDay)+" 00:00:00", '%Y-%m-%d %H:%M:%S')
    re_date_str = (day + offset).strftime('%Y-%m-%d %H:%M:%S')
    re_date = dt.strptime(re_date_str ,'%Y-%m-%d %H:%M:%S')
    a = datetime.date(re_date.year,re_date.month,day=1)
    return a.strftime('%Y-%m-%d %H:%M:%S')



# 定义一个函数，用来替换字符串中的变量
def replace_vars(s, d):
    # 使用 re.findall 函数，找出所有 ${cde_config} 包裹的变量
    vars = re.findall(r"\$\{([^\}]+)\}", s)
    # 遍历每个变量
    for var in vars:
        # 如果变量在 dict 中存在，就用 dict 中的值替换字符串中的变量
        if var in d:
            s = s.replace("${" + var + "}", str(d[var]))
        # 否则，就用空字符串替换字符串中的变量
        else:
            s = s.replace("${" + var + "}", "")
    # 返回替换后的字符串
    return s

# 调用函数，打印结果
print(replace_vars(s, d))


class TestGit(unittest.TestCase):

    def test_base(self):
        print("aaaaab".endswith("b"))


    def test_pd(self):
        # 导入pandas库
        import pandas as pd

        # 创建一个日期范围，从2023-12-31 00:00:00 到 2024-12-31 00:00:00，每天一个日期
        date_range = pd.date_range(start='2023-12-31 00:00:00', end='2024-12-31 00:00:00', freq='D')

        # 创建一个空的数据框，用于存储结果
        df = pd.DataFrame()

        # 将日期范围作为d_date列添加到数据框中
        df['d_date'] = date_range

        # 从d_date列中提取年份和月份，组合成c_yearmonth列
        df['c_yearmonth'] = df['d_date'].dt.strftime('%Y%m')

        df['d_ls_date'] = df.apply(getFirstDay,axis=1)

        # 计算d_date列中每个日期的上个月的最后一天，作为last_end_date列
        df['d_le_date'] = df.apply(getEndDay,axis=1)

        df['d_date'] = df.apply(date_format,axis=1)

        df['d_le_date_p'] = df['d_le_date']

        df.to_excel("C:\\Users\\xiaow\\Desktop\\sql\\dwd_cnmdb_dds_msd.xlsx",index=False)


if __name__ == '__main__':
    unittest.main()
