from datetime import datetime, timedelta
import unittest



class TestGit(unittest.TestCase):

    def test_base(self):
        check_day = "2023-11-10 00:00:00"
        print(check_day)
        date = datetime.strptime(check_day, "%Y-%m-%d %H:%M:%S")
        yesterday = date - timedelta(days=1)
        yesterday_str = yesterday.strftime("%Y-%m-%d %H:%M:%S")
        print(yesterday_str)

if __name__ == '__main__':
    unittest.main()
