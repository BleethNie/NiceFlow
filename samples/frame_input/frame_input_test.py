import unittest

import duckdb
import pandas as pd

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestFrameInput(unittest.TestCase):

    def test_frame_input_1(self):
        path = "faker_input.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()
        result_dict = myFlow.get_result()
        duck_df = list(result_dict.values())[0]


        path = "frame_input.json"
        myFlow2: Flow = FlowManager.read(path)
        myFlow2.set_result("frame_input",duck_df)
        myFlow2.run()




    def test_frame_input(self):
        path = "frame_input.json"

        df = pd.read_csv("che_test_2.csv")
        duck_df2 = duckdb.from_df(df)
        myFlow3: Flow = FlowManager.read(path)
        myFlow3.set_result("frame_input",duck_df2)
        myFlow3.run()