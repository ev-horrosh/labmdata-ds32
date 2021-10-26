import pandas as pd
import numpy as np


def null_count(df):
    return df.isnull().sum().sum()


def split_dates(date_series):
    df = pd.DataFrame(date_series)
    df[0] = pd.to_datetime(df[0])
    #     # df['column']
    for d in df:
        df["month"] = df[0].dt.month
        df["day"] = df[0].dt.day
        df["year"] = df[0].dt.year
        df = df.drop(columns=0)
    return df


def list_2_series(list_2_series, df):
    series = pd.Series(list_2_series)
    df = pd.DataFrame(series)
    return df
