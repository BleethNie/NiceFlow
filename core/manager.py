import importlib
import inspect
import json
import os

from core.flow import Flow
from core.plugin import IPlugin


# https://github.com/srn-g/pypluginbase/blob/main/src/PluginManager.py
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
    def discover_plugins(cls):
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
                    print("clazz", clazz, "是子类")
                    cls.registered_plugins_dict[clazz.__name__] = clazz

    @classmethod
    def get_register_plugins(cls):
        print(cls.registered_plugins_dict)

    @classmethod
    def execute_plugin(cls, plugin_name):
        clazz = cls.registered_plugins_dict[plugin_name]
        obj: IPlugin = clazz()
        obj.execute()



class FlowManager():
    __flowManagerDict: dict[str, Flow] = []

    @classmethod
    def read(cls, json_path: str):
        with open(json_path, 'r', encoding='utf8') as fp:
            flow_json = json.load(fp)
        nodes_array: json = flow_json["nodes"]
        for node in nodes_array:
            id = node["id"]
            type = node["type"]
            name = node["name"]
            properties = node["properties"]
            node_cls = importlib.import_module(type + '.' + id)

#
# JSONArray
# contents = job.getJSONArray("contents");
# FlowApp
# flowApp = create();
# for (int i = 0; i < contents.size(); i++) {
# JSONObject object = contents.getJSONObject(i);
# String id = object.getStr("id");
# AbstractPlugin p = FlowPluginManager.getFlowPluginManager().getPlugin(id);
# AbstractPlugin plugin = (AbstractPlugin) object.toBean(p.getClass());
# if (!StrUtil.isBlank(plugin.getFlowUid())) {
# flowApp.setFlowUid(plugin.getFlowUid());
# registeredFlows.remove(flowApp.getFlowUid());
# registeredFlows.put(flowApp.getFlowUid(), flowApp);
# } else {
# plugin.setFlowUid(flowApp.getFlowUid());
# }
# plugin.setType(p.type);
# flowApp.getFlowPlugins().put(plugin.getName(), plugin);
# }
# return flowApp;
