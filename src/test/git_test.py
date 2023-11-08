import unittest

import duckdb
import git


class TestGit(unittest.TestCase):

    def test_base(self):
        clone_repo=git.Repo.clone_from('https://github.com/gitpython-developers/GitPython.git','git/cmd.py') #拉取远程代码



if __name__ == '__main__':
    unittest.main()
