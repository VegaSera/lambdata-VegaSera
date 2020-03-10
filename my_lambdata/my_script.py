#my_lambdata/my_script.py
import pandas as pd
from my_mod import DataFrameSplitter

dataframe = pd.read_csv('https://drive.google.com/uc?export=download&id=13_tP9JpLcZHSPVpWcua4t2rY44K_s4H5')

x, y, z = DataFrameSplitter(dataframe).tvt_split()

print(x.shape, y.shape, z.shape)