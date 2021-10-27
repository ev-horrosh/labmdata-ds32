import pandas as pd
import numpy as np


def null_count(df):
    return df.isnull().sum().sum()

class SplitDates:
    '''
    Splits datatime into month, day, year.
    Takes a datetime series column,
    splits it and gets rid of original column
    '''

    def __init__(self, date_series):
        self.date_series=date_series
        
    def split_dates(self.date_series):

        df = pd.DataFrame(self.date_series)
        df[0] = pd.to_datetime(df[0])
        for d in df:
            df["month"] = df[0].dt.month
            df["day"] = df[0].dt.day
            df = df.drop(columns=0)
        return df


def list_2_series(list_2_series, df):
    series = pd.Series(list_2_series)
    df = pd.DataFrame(series)
    return df


if __name__=='__main__':
    