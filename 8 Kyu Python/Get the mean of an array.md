# Get the mean of an array

It's the academic year's end, fateful moment of your school report. The averages must be calculated. All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.

Return the average of the given array rounded down to its nearest integer.

The array will never be empty.

# Given Code

```{python}
def get_average(marks):
    raise NotImplementedError("TODO: get_average")

```

# My Solution

```{python}
from math import floor
from statistics import mean

def get_average(marks):
    return floor(mean(marks))
```
