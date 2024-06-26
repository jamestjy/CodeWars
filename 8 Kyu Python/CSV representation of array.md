# CSV representation of array

Create a function that returns the CSV representation of a two-dimensional numeric array.

Example:

```{python}
input:
   [[ 0, 1, 2, 3, 4 ],
    [ 10,11,12,13,14 ],
    [ 20,21,22,23,24 ],
    [ 30,31,32,33,34 ]] 
    
output:
     '0,1,2,3,4\n'
    +'10,11,12,13,14\n'
    +'20,21,22,23,24\n'
    +'30,31,32,33,34'
```

Array's length > 2.

More details here: https://en.wikipedia.org/wiki/Comma-separated_values

Note: you shouldn't escape the \n, it should work as a new line.

# Given Code

```{python}
def to_csv_text(array):
    pass
    # good luck
```

# My Solution

```{python}
def to_csv_text(array):
    formatted_rows = []

    for row in array:
        formatted_row = ','.join(map(str, row))
        formatted_rows.append(formatted_row)

    return '\n'.join(formatted_rows)
```
