import importlib.util
import inspect

import duckdb


def load_module(module_path):
    spec = importlib.util.spec_from_file_location("module", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def register_user_function(function_path, connection: duckdb.DuckDBPyConnection):
    module = load_module(function_path)
    items = inspect.getmembers(module, inspect.isfunction)
    for item in items:
        connection.create_function(item[0], item[1])


def register_sys_function(connection: duckdb.DuckDBPyConnection):
    # 注册系统函数
    module = importlib.import_module("NiceFlow.core.functions")
    items = inspect.getmembers(module, inspect.isfunction)
    for item in items:
        connection.create_function(item[0], item[1])
