import unittest

from NiceFlow.core.flow import Flow
from NiceFlow.core.manager import FlowManager


class TestFsSpecInput(unittest.TestCase):

    def test_fs_spec_input_1(self):
        path = "fsspec_input_ftp_console.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()


    def test_fs_spec_input_2(self):
        path = "fsspec_input_http_console.json"
        myFlow: Flow = FlowManager.read(path)
        myFlow.run()



if __name__ == '__main__':
    unittest.main()
