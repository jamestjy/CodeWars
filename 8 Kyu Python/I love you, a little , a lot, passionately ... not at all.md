# I love you, a little , a lot, passionately ... not at all

Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each of the following phrases each time a petal was torn:

- 1. "I love you"
- 2. "a little"
- 3. "a lot"
- 4. "passionately"
- 5. "madly"
- 6. "not at all"
     
If there are more than 6 petals, you start over with "I love you" for 7 petals, "a little" for 8 petals and so on.

When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.

Your goal in this kata is to determine which phrase the girls would say at the last petal for a flower of a given number of petals. The number of petals is always greater than 0.

# Given Code

```{python}
def how_much_i_love_you(nb_petals):
    # your code
```

# My Solution

```{python}
def how_much_i_love_you(nb_petals):
    output = nb_petals % 6
    match output:
        case 0:
            return "not at all"
        case 1:
            return "I love you"
        case 2:
            return "a little"
        case 3:
            return "a lot"
        case 4:
            return "passionately"
        case 5:
            return "madly"
```
