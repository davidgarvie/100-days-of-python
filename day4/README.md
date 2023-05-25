# Day 4

Important part today was related to modules. We use the `import` keyword

```py
import random
```

## Methods
- `random.random` - generates a random float between `0` and `1`
- `random.randint(a, b)` - generates a random int between `a` and `b` (inclusive)
- `random.choice(list)` - will pick an item from a list at a random index

## Lists
A list is a way to link data together. It uses square bracket notation
```py
names = ["Ron", "Leslie", "Tom"]
```

Note, lists can contain different types and can also include nested lists
```py
things = ["apple", 5, False]

numbers = [1, 2, 3]
names = ["Ron", "Leslie", "Tom"]
lists = [numbers, names] # [[1, 2, 3], ['Ron', 'Leslie', 'Tom']]
```

## Useful links
[Python data structures](https://docs.python.org/3/tutorial/datastructures.html)
