import pandas as pd
import numpy as np


class Helper:
    """
    split_dates()
    Splits datatime into month, day, year.
    Takes a datetime series column,
    splits it and gets rid of original column
    """

    def __init__(self, date_series):
        self.date_series = date_series

    def split_dates(date_series):

        df = pd.DataFrame(date_series)
        df[0] = pd.to_datetime(df[0])
        for d in df:
            df["month"] = df[0].dt.month
            df["day"] = df[0].dt.day
            df = df.drop(columns=0)
        return df

    def null_count(date_series):
        return date_series.isnull().sum().sum()


# def list_2_series(list_2_series, df):
#     series = pd.Series(list_2_series)
#     df = pd.DataFrame(series)
#     return df

if __name__ == "__main__":

    # df = Helper.split_dates(pd.Series(["1/12/2006", "2/10/2017", np.nan]))
    # df = Helper.null_count(pd.Series(["1/12/2006", "2/10/2017", np.nan]))
    # print(df)
