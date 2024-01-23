import re
import time
from loguru import logger
import datetime
import random

class XTimer:

    @classmethod
    def plugin(cls, func):
        def wrapper(*args, **kwargs):
            s_time = time.time()
            res = func(*args, **kwargs)
            e_time = time.time()
            diff = e_time - s_time
            logger.info('【{}】插件执行耗时【{}】秒'.format("plugin", diff))
            return res

        return wrapper


# 提取变量
def extract_variable(s):
    pattern = r'\$\{(.*?)\}'
    matches = re.findall(pattern, s)
    return matches


s = '${file_name}'
print(extract_variable(s))  # 输出: ['file_name']


# 定义一个函数，用来替换字符串中的变量
def replace_vars(s: str, d: dict):
    """
    s:需要替换变量的字符串
    d:替换字符

    示例：
    s = "Hello, ${row.name}. Your age is ${row.age}. Your favorite color is ${color}."
    d = {"row": {"name": "Alice", "age": 25}, "color": "red"}

    输出:
    Hello, Alice. Your age is 25. Your favorite color is red.
    """
    # 使用 re.findall 函数，找出所有 ${cde_config} 包裹的变量

    vars = re.findall(r"\$\{([^\}]+)\}", str(s))
    # 遍历每个变量
    if len(vars)==0:
        return s,False
    for var in vars:
        # 使用 eval 函数，尝试从 dict 中获取变量的值
        try:
            value = d[var]
        # 如果出现异常，就用空字符串替换字符串中的变量
        except:
            value = ""
        # 用变量的值替换字符串中的变量
        s = s.replace("${" + var + "}", str(value))
    # 返回替换后的字符串
    return s,True


def random_str()->str:

    # 获取当前时间，精确到毫秒
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    # 生成一个5位的随机码
    random_code = ''.join(random.sample('0123456789', 5))
    # 将时间和随机码拼接在一起
    result = f"{current_time}_{random_code}"
    return result


if __name__ == '__main__':
    s = "Hello, ${row.name}. Your age is ${row.age}. Your favorite color is ${color}."
    d = {"row.name":  "Alice", "row.age": 2, "color": "red"}
    ss = replace_vars(s,d)
    print(ss)