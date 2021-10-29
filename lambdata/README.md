# Collection of helper functions based on numpy and pandas libraries.

These functions intend to speed up some aspects of the data science workflow.

## What's inside:

`split_dates()` - Splits Datatime strings into month, day, year.Takes a datetime series column,splits it and gets rid of original column

```python
from helper_functions import split_dates
series=pd.Series([["1/12/2006", "2/10/2017"]])

df_dates=split_dates(series)
```
Output:

| day  | month | year |
|:----:|:-----:|:----:|
|  12  |   1   | 2006 |
|  10  |   2   | 2017 |

`list_2_series()`- Takes list and appends in to df.

```python
from helper_functions import list_2_series

mylist=['test',2345,5.5,,0,np.nan]
df = list_2_series(mylist)
```
Output:

| my_list |
|:-------:|
|   test  |
|   2345  |
|   5.5   |
|    0    |
|   NaN   |

## Licence 

MIT © [Ev-horrosh]()