# Collection of helper functions based on numpy and pandas libraries.

These functions intend to speed up some aspects of the data science workflow.

What's inside:

`split_dates()` - Splits Datatime into month, day, year.T
akes a datetime series column,splits it and gets rid of original column

```python
series=pd.Series([["1/12/2006", "2/10/2017"]])

df_dates=split_dates(series)

Output:

| day  | month | year |
|:----:|:-----:|:----:|
|  12  |   1   | 2006 |
|  10  |   2   | 2017 |

```
output:

| day  | month | year |
|:----:|:-----:|:----:|
|  12  |   1   | 2006 |
|  10  |   2   | 2017 |

`list_2_series()`- Takes list and appends in to df.

