import abc
import json


class IPlugin(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    def init(self, param: json):
        print(param)

    @abc.abstractmethod
    def execute(self):
        pass
