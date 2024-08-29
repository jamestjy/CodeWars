# Logical calculator

## Your Task

Given an array of Boolean values and a logical operator, return a Boolean result based on sequentially applying the operator to the values in the array.

## Examples

1. booleans = [True, True, False], operator = "AND"
- True AND True -> True
- True AND False -> False
- return False

2. booleans = [True, True, False], operator = "OR"
- True OR True -> True
- True OR False -> True
- return True

3. booleans = [True, True, False], operator = "XOR"
- True XOR True -> False
- False XOR False -> False
- return False

## Input

1. an array of Boolean values (1 <= array_length <= 50)
2. a string specifying a logical operator: "AND", "OR", "XOR"

## Output

A Boolean value (True or False).

# Given Code

```{python}
def logical_calc(array, op):
    return True
```

# My Solution

```{python}
def logical_calc(array, op):
    match op:
        case "AND":
            return all(array)
        case "OR":
            return any(array)
        case "XOR":
            res = array[0]
            for i in array[1:]:
                res  ^= i
            return res
```
