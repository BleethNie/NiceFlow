import unittest

import duckdb
# 定义一个字符串，包含多个 ${cde_config} 包裹的变量
s = "Hello, ${row.name}. Your age is ${row_age}. Your favorite color is ${color}."

# 定义一个 dict，用来存储变量的值
d = {"row.name": "AAAA", "row_age": 25, "color": "red"}

# 导入 re 模块，用来进行正则表达式匹配
import re

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


if __name__ == '__main__':
    unittest.main()
