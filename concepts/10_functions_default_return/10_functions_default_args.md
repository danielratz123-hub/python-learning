# Functions — Default Arguments

## What it is
A default argument is a fallback value a parameter uses if no value is
passed in when the function is called.

## Syntax
```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Joe")                 # "Hello, Joe!"       (uses default)
greet("Joe", "Good morning") # "Good morning, Joe!" (overrides default)
```

## Rules
- Default parameters must come *after* non-default parameters in the
  function definition:
```python
def example(a, b=5):   # valid
    pass

def broken(a=5, b):     # SyntaxError! a can't have a default before b doesn't
    pass
```

## Keyword arguments
You can pass arguments by name, which lets you skip the positional order:
```python
def describe(name, age, city="Tel Aviv"):
    print(f"{name}, {age}, from {city}")

describe(name="Joe", city="Haifa", age=22)  # order doesn't matter here
```

## Common pitfalls
- Using a mutable default value like a list or dict (`def f(items=[])`) —
  this is a classic Python gotcha. The same list gets reused across every
  call instead of creating a fresh one each time. Safer pattern:
```python
def f(items=None):
    if items is None:
        items = []
```
- Forgetting that once you use a keyword argument, all arguments after it
  in the call must also be keyword arguments.
