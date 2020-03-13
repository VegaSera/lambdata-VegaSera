# lambdata-VegaSera

##Example Script

We have two functions, each using a pandas dataframe.


###Train, Validate, Test split with tvt_split()
```
import pandas as pd

dataframe = pd.read_csv(**URL TO DATAFRAME**)

splitter = DataFrameSplitter(dataframe)
train, validate, test = splitter.tvt_split(split=0.2)
```

This function returns three dataframes, with a specified size for Validate and Test. 

If the size of the split is a float between 0 and 0.5, then the method will treat it as a percentage of the total dataframe and set the size of validate and test to that amount.

If the size of the split is an integer smaller than half of the size of the initial dataframe, then it will give validate and test dataframes with a size equal to that integer.

If for some reason you provide a float or an int outside of the above scope, or any other value, the method will default to 0.1 and warn you.

If for instance you wanted a train/validate/test split that were perfectly equal (assuming the dataframe is evenly divisible by three) then you can use tvt_split(split=0.33333).

### Datetime Split with datetime_split()
**The dataframe you pass in must have at least one column that is of a pandas datetime format already.**
```
dataframe = pd.read_csv(**URL TO DATAFRAME**)

dataframe['DATETIME_COLUMN'] = pd.to_datetime(dataframe['DATETIME_COLUMN']

splitter = DataFrameSplitter(dataframe)
new_dataframe = splitter.datetime_split(remove_old = False)

```
This will return a new dataframe that matches the old, but includes new columns for Year, Month, Day, Hour, Minute, and Second, if the column has more than one unique value(i.e. has relevant data).

For example, if you had a datetime column that recorded year, month, and day, but all of the hour, minute, and second fields were 00:00:00, the dataframe you receive will only have Year, Month, and Day added to it.

the `remove_old =` parameter allows you to choose whether or not to remove the original datetime column or not. If set to `True`, then the dataframe you get back will not include the total datetime column, only the new, separated columns.
