# Basic subclasses - Adam and Eve

According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.

You have to do God's job. The creation method must return an array of length 2 containing objects (representing Adam and Eve). The first object in the array should be an instance of the class Man. The second should be an instance of the class Woman. Both objects have to be subclasses of Human. Your job is to implement the Human, Man and Woman classes.

# Given Code

```{python}
def God():
    #code

#code
```

# My Solution

```{python}
def God():
    return [Man(), Woman()]

class Human(object):
    pass

class Man(Human):
    pass
    
class Woman(Human):
    pass
```