
# my_lambdata/my_mod.py

from sklearn.model_selection import train_test_split
import pandas as pd

#Train, Validate, Test split
def tvt_split(df, split=0.1):
    """
    Takes a Pandas DataFrame
    Returns three DataFrames with equal sized validate and test.
    Size of the split can be changed with the `split=` argument. Default is 0.1
    Split must be either a float between 0 and 0.5, or an int smaller than half of the dataframe length. 

    """
    init_df_len = len(df)

    #Type handling and correction
    if type(split) == float:
        if split < 0.5:
            split_num = int(init_df_len * split)
        else:
            print('Error - Split provided was a float greater than or equal to 0.5. Setting split to default 0.1')
            split_num = int(init_df_len * 0.1)
    elif type(split) == int:
        if split < (init_df_len/2):
            split_num = split
        else:
            print(f'Error - Split provided was an int greater than or equal to half the length of the DataFrame ({init_df_len})')
            print('Setting split to default - 0.1')
            split_num = int(init_df_len * 0.1)
    else:
        print(f'Error - Split provided was of an unacceptable type - {type(split)}. Split must either be a float between 0 and 0.5, or an int smaller than half of the length of the dataframe.')
        print('Setting split to default - 0.1')
        split_num = int(init_df_len * 0.1)
    
    train, validate = train_test_split(df, test_size = split_num)
    train, test = train_test_split(train, test_size = split_num)

    return train, validate, test

def datetime_split(df, remove_old = False):
    """
    At least one column in the dataframe must be of a Datetime object.
    Convert the specified columns to datetime with pd.to_datetime(column)

    remove_old - Removes original columns and leaves only the split version. Default False
    """
    #Intelligently determine if any of the columns can be converted to datetime, including unix datetime.
    #If so, convert it, split it, and optionally remove the old column.
    
    #Get all columns with datetime object types.
    collist = []
    for col in df.columns:
        if pd.core.dtypes.common.is_datetime_or_timedelta_dtype(df[col]):
            collist.append(col)
    
    
    if len(collist) == 0: #If the list is empty, then there were no columns using datetime objects.
        print('No columns of datetime format found. Try using pd.to_datetime(column) on your date columns.')
    else:
        for col in collist:
            #Every datetime column in the dataframe gets split into its component parts, but only if it contains more
            # than one unique value.
            if len(df[col].dt.year.unique()) > 1:
                df[f'{col}.year'] = df[col].dt.year
            if len(df[col].dt.month.unique()) > 1:
                df[f'{col}.month'] = df[col].dt.month
            if len(df[col].dt.day.unique()) > 1:
                df[f'{col}.day'] = df[col].dt.day
            if len(df[col].dt.hour.unique()) > 1:
                df[f'{col}.hour'] = df[col].dt.hour
            if len(df[col].dt.minute.unique()) > 1:
                df[f'{col}.minute'] = df[col].dt.minute
            if len(df[col].dt.second.unique()) > 1:
                df[f'{col}.second'] = df[col].dt.second
            
            if remove_old: #If the remove_old flag is true, gets rid of the old column
                df = df.drop(col, axis=1)
        
        return df





if __name__ == "__main__":
    #Runs only if the file is run directly, rather than imported.
    pass
