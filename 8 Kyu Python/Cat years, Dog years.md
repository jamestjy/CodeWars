# Cat years, Dog years

## Kata Task
I have a cat and a dog.

I got them at the same time as kitten/puppy. That was humanYears years ago.

Return their respective ages now as [humanYears,catYears,dogYears]

NOTES:

humanYears >= 1
humanYears are whole numbers only

## Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that

## Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that

## References

http://www.catster.com/cats-101/calculate-cat-age-in-cat-years
http://www.slate.com/articles/news_and_politics/explainer/2009/05/a_dogs_life.html
If you liked this Kata there is another related one here

# Given Code

```{python}
def human_years_cat_years_dog_years(human_years):
    # Your code here
    return [0,0,0]
```

# My Solution

```{python}
def human_years_cat_years_dog_years(human_years):
    cat_years = 0
    dog_years = 0
    match human_years:
        case 1:
            cat_years = dog_years = 15
        case 2:
            cat_years = dog_years = 15 + 9
        case _:
            cat_years = 15 + 9 + 4 * (human_years - 2)
            dog_years = 15 + 9 + 5 * (human_years - 2)
    return [human_years, cat_years, dog_years]
```
