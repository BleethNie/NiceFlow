import abc



class IPlugin(metaclass=abc.ABCMeta):

    def __init__(self):
        pass


    def init(self, param: dict):
        """
            初始化参数
        """
        pass



    @abc.abstractmethod
    def execute(self):
        pass
