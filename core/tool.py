import time


class timer():
    def __init__(self, flow='', plugin=''):
        self.flow = flow
        self.plugin = plugin

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            s_time = time.time()
            func(*args, **kwargs)
            e_time = time.time()
            diff = e_time - s_time
            if self.plugin is not "":
                print('【{}】插件执行耗时【{}】秒'.format(self.plugin, diff))
            if self.flow is not "":
                print('【{}】任务执行耗时【{}】秒'.format(self.flow, diff))
        return wrapper
