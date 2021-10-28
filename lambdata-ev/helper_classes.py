import pandas as pd
import numpy as np


class Helper:
    def __init__(self, df):
        self.df = df

    def split_dates(df):
        """
        Splits datatime into month, day, year.
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

    def null_count(df):
        """counts null values in dataframe
        Args:
            df: Series or Dataframe
        Returns:
            int: number of null values
        """
        return df.isnull().sum().sum()


class List2Series:
    def __init__(self, list_2_series):
        self.list_2_series = list_2_series

    def list_2_series(list_2_series):
        series = pd.Series(list_2_series)
        df = pd.DataFrame(series, columns=["your list"])
        return df


if __name__ == "__main__":
    # TESTING
    user_input = (input("provide somethin: ")).lower().split(",")
    df = List2Series.list_2_series(user_input)

    # df = Helper.split_dates(pd.Series(["1/12/2006", "2/10/2017"]))
    # df = Helper.null_count(pd.Series(["1/12/2006", "2/10/2017", np.nan]))
    # help(Helper.null_count)

    print(df)
