import unittest

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestESInput(unittest.TestCase):

    def test_es_input_to_console(self):
        path = "es_input_to_console.json"
        myFlow: Flow = FlowManager.read(path)
        flow_param = {
            "url": "http://192.168.1.90:9200",
            "index": "test",
            "query": '''{
                "query":{
                    "match_all":{}
                }
            }'''
        }
        myFlow.set_param(flow_param)
        myFlow.run()

        result_dict = myFlow.get_result()
        duck_df = list(result_dict.values())[0]
        print(duck_df)


    def test_es_input_to_console_es_output(self):
        path = "es_input_to_console_es_output.json"
        myFlow: Flow = FlowManager.read(path)
        flow_param = {
            "url": "http://127.0.0.1:9200",
            "index": "test",
            "query": '''{
                "query":{
                    "match_all":{}
                }
            }'''
        }
        myFlow.set_param(flow_param)
        myFlow.run()



if __name__ == '__main__':
    unittest.main()
