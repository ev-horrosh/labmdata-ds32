from lambdata import helper_functions


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
