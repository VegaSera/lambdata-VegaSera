import unittest
import pandas as pd
from my_lambdata.my_mod import DataFrameSplitter


class DataFrameSplitterTester(unittest.TestCase):

    def test_tvt_split(self):
        df = pd.read_csv('https://drive.google.com/uc?export=download&id=13_tP9JpLcZHSPVpWcua4t2rY44K_s4H5')
        splitter = DataFrameSplitter(df)

        x = splitter.tvt_split()

        #Asserting that we get three dataframes back.
        self.assertEqual(len(x), 3)

        #Asserting that the Training dataframe is of an acceptable size.
        self.assertGreater(len(x[0]), 5)

        #Asserting that the Validation Dataframe is of an acceptable size.
        self.assertGreater(len(x[1]), 5)

        # Asserting that the Test Dataframe is of an acceptable size.
        self.assertGreater(len(x[2]), 5)

    def test_datetime_split(self):
        pass
        #Assert a given dataframe has a date time column with Years, Months, Days, Hours, Minutes, Seconds.

        #Assert a given dataframe has a date time column with Years, Months, Days, but no specific times.

        #Assert a given dataframe has no valid datetime column.

        #Run assertions to confirm each of the dataframes after being run through the method.

if __name__ == '__main__':
    unittest.main()