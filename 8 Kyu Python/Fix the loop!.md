# Fix the loop!

Your collegue wrote an simple loop to list his favourite animals. But there seems to be a minor mistake in the grammar, which prevents the program to work. Fix it! :)

If you pass the list of your favourite animals to the function, you should get the list of the animals with orderings and newlines added.

For example, passing in:
```
animals = [ 'dog', 'cat', 'elephant' ]
```

will result in:
```
list_animals(animals) == '1. dog\n2. cat\n3. elephant\n'
```

# Given Code

```{python}
def list_animals(animals):
    lst = ''
    for i in range(animals):
        lst += str(i + 1) + '. ' + animals[i] + '\n'
    return lst
```

# My Solution

```{python}
def list_animals(animals):
    lst = ''
    for i, animal in enumerate(animals, start=1):
        lst += f"{i}. {animal}\n"
    return lst
```
