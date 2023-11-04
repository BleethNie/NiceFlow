import importlib
import inspect
import json
import os
import sys

from NiceFlow.core.flow import Flow
from NiceFlow.core.plugin import IPlugin
from loguru import logger
import logging
from NiceFlow import plugins


class SingletonMeta(type):
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class PluginManager(metaclass=SingletonMeta):
    plugins_list: list = []

    registered_plugins_dict: dict = {}



    @classmethod
    def register_user_plugin(cls):
        """
        Find plugins from other directory
        """

        # 获取当前文件的绝对路径
        current_file = os.path.abspath(__file__)
        # 获取当前文件所在目录的绝对路径
        current_directory = os.path.dirname(current_file)
        # 获取当前项目的根目录
        project_root = os.path.dirname(os.path.dirname(current_directory))
        plugin_root_path = project_root + "/plugins"
        logger.info("开始扫描自定义插件安装目录{}",plugin_root_path)
        if not os.path.exists(plugin_root_path):
            os.makedirs(plugin_root_path)
            return
        # 动态加载可执行的python文件
        sys.path.append(plugin_root_path)

        for plugin_dir in os.scandir(plugin_root_path):
            if not plugin_dir.is_dir():
                continue
            for plugin_file in os.scandir(plugin_dir.path):
                head, plugin_file_name = os.path.split(plugin_file.path)
                plugin_name, extension = os.path.splitext(plugin_file_name)
                if plugin_file_name != 'plugin.py':
                    continue
                cls.plugins_list.append(plugin_name)
                cls.__register_plugin(plugin_name, "hello")

    @classmethod
    def register_plugin(cls):
        """
        Find plugins and add them to list
        """
        plugins_folder_path = os.path.dirname(plugins.__file__)
        for file_name in os.scandir(plugins_folder_path):
            if file_name.is_file():
                head, tail = os.path.split(file_name.path)
                plugin_name, extension = os.path.splitext(tail)
                if extension != '.py':
                    continue
                cls.plugins_list.append(plugin_name)
                cls.__register_plugin(plugin_name)

    @classmethod
    def __register_plugin(cls, plugin_name: str, plugins_folder_path=None):
        """
        Load the plugin and get its information
        """
        if plugin_name in cls.plugins_list:
            loaded_plugin: IPlugin
            if plugins_folder_path == None:
                module_str = f'NiceFlow.plugins.{plugin_name}'
            else:
                module_str = f'{plugins_folder_path}.{plugin_name}'
            try:
                module = importlib.import_module(module_str)
            except ModuleNotFoundError as e:
                print(e)
                logger.error('Flow注册组件【{}】失败,请先安装相关依赖', module_str)
                return
                # 获取python脚本中的所有类
            for name, clazz in inspect.getmembers(module, inspect.isclass):
                # 判断该类是不是IPlugin类的子类
                if issubclass(clazz, IPlugin) and clazz.__name__ != IPlugin.__name__:
                    logger.debug("Flow注册组件【{}】".format(clazz.__name__))
                    cls.registered_plugins_dict[clazz.__name__] = clazz

    @classmethod
    def get_plugin(cls, plugin_name: str) -> IPlugin:
        clazz = cls.registered_plugins_dict[plugin_name]
        obj: IPlugin = clazz()
        return obj

    @classmethod
    def execute_plugin(cls, plugin_name: str):
        clazz = cls.registered_plugins_dict[plugin_name]
        obj: IPlugin = clazz()
        obj.before_execute()
        obj.execute()


class FlowManager(metaclass=SingletonMeta):
    flow_manager_dict: dict[str, Flow] = {}

    # 注册系统插件
    PluginManager.register_plugin()
    PluginManager.register_user_plugin()

    @classmethod
    def read(cls, json_path: str) -> Flow:
        flow = Flow()
        cls.flow_manager_dict[flow.flow_uid] = flow
        with open(json_path, 'r', encoding='utf8') as fp:
            flow_json = json.load(fp)
        nodes_array: json = flow_json["nodes"]
        edges_array: json = flow_json["edges"]
        # 组装node,edge
        for node_json in nodes_array:
            node_id: str = node_json["id"]
            node: IPlugin = PluginManager.get_plugin(node_id)
            node.init(node_json, flow)
            flow.add_node(node)
            logger.info("Flow Node创建完成【{}--{}】".format(node.id, node.name))
        for edge in edges_array:
            flow.set_edge(edge["startId"], edge["endId"])

        return flow
