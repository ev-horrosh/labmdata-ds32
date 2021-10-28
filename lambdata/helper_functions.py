import numpy as np
import pandas as pd


def split_dates(df):
    """Splits datatime into month, day, year.
    Takes a datetime series column,
    splits it and gets rid of original column
    """
    df = pd.DataFrame(df)
    df[0] = pd.to_datetime(df[0])
    for d in df:
        df["month"] = df[0].dt.month
        df["day"] = df[0].dt.day
        df["year"] = df[0].dt.year
        df = df.drop(columns=0)
    return df

# df = split_dates(pd.Series(["1/12/2006", "2/10/2017"]))
# print(df)


def list_2_series(list_2_series):
    series = pd.Series(list_2_series)
    df = pd.DataFrame(series, columns=["your list"])
    return df

# df = list_2_series(['test',2345,5,'f',0,np.nan])
# print(df)