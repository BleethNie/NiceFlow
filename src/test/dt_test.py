'''PyODPS 3
Please try your best avoiding downloading massive data from MaxCompute. Related methods are `open_reader` of tables or instances, and `to_pandas` of DataFrames. 
It is recommended to use PyODPS DataFrame created from MaxCompute tables, or MaxCompute SQL directly. Reference：https://www.alibabacloud.com/help/doc-detail/90481.htm
'''


import datetime
from datetime import datetime as dt


def getYesterday():
    yesterday = datetime.date.today() + datetime.timedelta(-1)
    return yesterday.strftime('%Y-%m-%d')+" 00:00:00"


def get_yesterday_23():
    today = datetime.date.today()
    year = today.year
    month = today.month
    day = today.day
    today_0 = datetime.datetime(year, month, day)
    yesterday_23 = today_0 - datetime.timedelta(hours=1)
    date_str = yesterday_23.strftime("%Y-%m-%d %H:%M:%S")
    return date_str


def get_today_5():
    today = datetime.date.today()
    year = today.year
    month = today.month
    day = today.day
    today_5 = datetime.datetime(year, month, day, 5)
    date_str = today_5.strftime("%Y-%m-%d %H:%M:%S")
    return date_str



def is_in_time_range(time_str, start_str, end_str):
    time_format = "%Y-%m-%d %H:%M:%S"
    # 尝试将时间字符串转换为datetime对象，如果失败则抛出异常
    try:
        time = datetime.datetime.strptime(time_str, time_format)
        start = datetime.datetime.strptime(start_str, time_format)
        end = datetime.datetime.strptime(end_str, time_format)
    except ValueError as e:
        print("无效的时间字符串:", e)
        return False
    # 判断time是否在start和end之间（包含边界），并返回结果
    return start <= time <= end



def time_timedelta(current_str,task_time_str,timedelta_second):
    fmt = '%Y-%m-%d %H:%M:%S'
    current_date = dt.strptime (current_str, fmt)
    task_time_date = dt.strptime (task_time_str, fmt)
    td = current_date - task_time_date
    if td.total_seconds () >= timedelta_second:
        print ('时间差是', td, ',超过20分钟')
        return True
    return False


def compare_time_str(time_str1, time_str2):
    # 定义一个时间格式，用于解析时间字符串
    # 这里假设时间字符串的格式是"年-月-日 时:分:秒"，例如"2023-11-15 09:36:22"
    # 如果您的时间字符串有不同的格式，您需要修改这个时间格式
    time_format = "%Y-%m-%d %H:%M:%S"

    # 尝试将时间字符串转换为datetime对象，如果失败则抛出异常
    try:
        time1 = datetime.datetime.strptime(time_str1, time_format)
        time2 = datetime.datetime.strptime(time_str2, time_format)
    except ValueError as e:
        print("无效的时间字符串:", e)
        return None

    # 比较time1和time2的大小，并返回结果
    if time1 < time2:
        return -1
    elif time1 == time2:
        return 0
    else:
        return 1

def check_task():
    task_list = [
        ("select job_start_time as task_time from config_sync_incr_cnmdb where sync_type = -1",1200,"config_sync_incr_cnmdb任务"),
        ("select job_start_time as task_time from config_sync_incr_cnmdb_realtime where sync_type = -1",1200,"config_sync_incr_cnmdb_realtime任务"),
        ("select job_start_time as task_time from config_sync_incr_month where sync_type = -1",2460,"config_sync_incr_month任务"),
        ("select job_start_time as task_time from config_sync_incr_mysql where sync_type = -1",86460,"config_sync_incr_mysql任务"),
        ("select job_start_time as task_time from config_analyse_sale where job_type = 1",1200,"config_analyse_sale任务【流程名称analyse_sale_total】"),
        ("select job_start_time as task_time from config_sync_incr_compensation where sync_type = -1",1200,"config_sync_incr_compensation任务")
    ]

    error_message = ''
    for item in task_list:
        sql = item[0]
        timedelta_second = item[1]
        task_name = item[2]
        now_str  = dt.now().strftime('%Y-%m-%d %H:%M:%S')
        task_time_str = '2023-11-15 09:00:00'
        if "config_sync_incr_month" in  task_name:
            if is_in_time_range(now_str,get_yesterday_23() , get_today_5()):
                continue
        is_error = time_timedelta(now_str,task_time_str,timedelta_second)
        if is_error:
            error_message = error_message+"【数据同步任务】{} 最后一次执行时间 {},检测到任务暂停，需要手动检查\r\n".format(task_name,task_time_str)
    return error_message


if __name__ == '__main__':
    print(compare_time_str("2023-11-15 00:00:01","2023-11-15 00:00:00"))
