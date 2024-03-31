import unittest

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestFakerInput(unittest.TestCase):

    def test_faker(self):
        path = "faker_input_csv_output.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()


if __name__ == '__main__':
    unittest.main()
