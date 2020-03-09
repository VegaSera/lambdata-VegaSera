#my_lambdata/my_script.py

import pandas as pd
from my_lambdata.my_mod import enlarge

print('HELLO WORLD')

df = pd.DataFrame({'state': ['CT','CO', 'CA', 'AZ']})

print(df.head())

x=5
print('ENLARGED = ', enlarge(x))