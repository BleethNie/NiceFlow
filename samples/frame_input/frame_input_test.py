import unittest

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestFrameInput(unittest.TestCase):

    def test_frame_input(self):
        path = "faker_input.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()
        result_dict = myFlow.get_result()
        duck_df = list(result_dict.values())[0]


        path = "frame_input.json"
        myFlow2: Flow = FlowManager.read(path)
        myFlow2.set_result("frame_input",duck_df)
        myFlow2.run()

        myFlow3: Flow = FlowManager.read(path)
        myFlow3.set_result("frame_input",duck_df)
        myFlow3.run()