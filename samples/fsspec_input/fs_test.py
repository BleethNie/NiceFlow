import unittest

import petl
from fsspec.implementations.git import GitFileSystem
from fsspec.implementations.sftp import SFTPFileSystem
from webdav4.client import Client


class TestFsSpecInput(unittest.TestCase):

    def test_fs_webdav(self):
        client = Client("http://192.168.1.89/webdav")
        res = client.ls("/", detail=False)
        print(res)
        res = client.info("/che_test_2.csv")
        print(res)

    def test_fs_sftp(self):
        params = {"username": "root", "password": "root@123123", }
        client = SFTPFileSystem(host="192.168.199.2", **params)
        res = client.ls("/tmp/che")
        print(res)
        res = client.info("/tmp/che/che_test_2.csv")
        print(res)
        res = client.stat("/tmp/che/che_test_2.csv")
        print(res)

    def test_fs_git(self):
        path="git://192.168.199.2:3000/bleeth/jc-go/README.md"
        client = GitFileSystem(path=path,ref="test")
        res = client.ls("/")
        print(res)

    def test_fs_smb(self):
        url = 'smb://user:password@server/share/folder/file.csv'
        data = b'foo,bar\na,1\nb,2\nc,2\n'
        petl.tocsv(data, url)
        tbl = petl.fromcsv(url)


if __name__ == '__main__':
    unittest.main()
