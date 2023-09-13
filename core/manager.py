import importlib
import inspect
import json
import os

from core.flow import Flow
from core.plugin import IPlugin


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

    plugins_folder_path = "plugins"

    @classmethod
    def register_plugin(cls):
        """
        Find plugins and add them to list
        """
        for file_name in os.scandir(cls.plugins_folder_path):
            if file_name.is_file():
                head, tail = os.path.split(file_name.path)
                plugin_name, extension = os.path.splitext(tail)
                if extension != '.py':
                    continue
                cls.plugins_list.append(plugin_name)
                cls.__register_plugin(plugin_name)

    @classmethod
    def __register_plugin(cls, plugin_name: str):
        """
        Load the plugin and get its information
        """
        if plugin_name in cls.plugins_list:
            loaded_plugin: IPlugin
            module_str = f'{cls.plugins_folder_path}.{plugin_name}'
            module = importlib.import_module(module_str)
            # 获取python脚本中的所有类
            for name, clazz in inspect.getmembers(module, inspect.isclass):
                # 判断该类是不是IPlugin类的子类
                if issubclass(clazz, IPlugin) and clazz.__name__ != IPlugin.__name__:
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
        obj.execute()


class FlowManager(metaclass=SingletonMeta):
    flow_manager_dict: dict[str, Flow] = {}

    # 注册系统插件
    PluginManager.register_plugin()

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
            node.init(node_json)
            flow.add_node(node)
        for edge in edges_array:
            flow.set_edge(edge["startId"], edge["endId"])
        return flow
