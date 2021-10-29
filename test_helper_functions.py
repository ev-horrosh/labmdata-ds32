"""Testinf helper functions"""
from lambdata import helper_functions as hf
import pandas as pd


def test_hf_type():
    """Testing if the output is a Dataframe"""
    assert type(hf.split_dates(pd.Series())) == type(pd.DataFrame())


def test_hf_same_output():
    """Testing if dataframes have the same output"""
    assert hf.split_dates(pd.Series(["1/12/2006"])).equals(
        pd.DataFrame({"month": 1, "day": 12, "year": 2006}, index=[0])
    )

def list_2_series(list_2_series):
    series = pd.Series(list_2_series)
    df = pd.DataFrame(series, columns=["your list"])
    return df

# df = list_2_series(['test',2345,5,'f',0,np.nan])
# print(df)