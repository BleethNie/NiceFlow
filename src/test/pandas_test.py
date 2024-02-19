import unittest

import pandas as pd
from pandas._libs.tslibs.offsets import MonthBegin, MonthEnd, CBMonthBegin, CBMonthEnd, BMonthBegin, \
    CustomBusinessMonthEnd
from pandas.tseries.offsets import BMonthEnd


class TestPandas(unittest.TestCase):

    # https://www.cnblogs.com/wwj99/p/12237947.html
    def test_base(self):
        pd.set_option('display.min_rows', 1000)
        df = pd.DataFrame()
        index = pd.date_range(start='2023-12-31', periods=366, freq='D').astype('str')+ " 00:00:00"
        index_2 = index.astype('datetime64[ns]') - MonthBegin()
        index_3 = index.astype('datetime64[ns]') + CustomBusinessMonthEnd()
        # index_4 = index.astype('datetime64[ns]') + CBMonthBegin()
        # index_5 = index.astype('datetime64[ns]') + CBMonthEnd()
        index_6 = index.astype('datetime64[ns]') - BMonthBegin()
        index_7 = index.astype('datetime64[ns]') + BMonthEnd()

        df["date"] = index
        df["date_2"] = index_2
        df["date_3"] = index_3
        # df["date_4"] = index_4
        # df["date_5"] = index_5
        df["date_6"] = index_6
        df["date_7"] = index_7

        df.to_clipboard()


if __name__ == '__main__':
    unittest.main()
