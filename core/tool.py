import time


class XTimer:

    @classmethod
    def plugin(cls, func):
        def wrapper(*args, **kwargs):
            s_time = time.time()
            res = func(*args, **kwargs)
            e_time = time.time()
            diff = e_time - s_time
            print('【{}】插件执行耗时【{}】秒'.format("plugin", diff))
            return res

        return wrapper
