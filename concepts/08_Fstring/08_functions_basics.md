# Functions — Parameters and Return Values

## What it is
A function is a reusable block of code that performs a task. Functions help
avoid repeating yourself and make code easier to test and organize.

## Defining and calling a function
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Joe")   # calling the function with an argument
```

## Parameters vs arguments
- **Parameter**: the placeholder name in the function definition (`name`)
- **Argument**: the actual value you pass in when calling (`"Joe"`)

## Return values
`return` sends a value back out of the function so it can be used elsewhere.
Without `return`, a function returns `None` by default.

```python
def add(a, b):
    return a + b

result = add(3, 4)   # result is 7
print(result)
```

## `print()` vs `return` — a key distinction
```python
def add_print(a, b):
    print(a + b)     # only displays the value, doesn't give it back

def add_return(a, b):
    return a + b      # gives the value back so it can be stored/used

x = add_print(3, 4)   # x is None!
y = add_return(3, 4)  # y is 7
```

## Common pitfalls
- Forgetting `return` and expecting the function's output to be usable —
  it isn't, if you only `print()` inside the function.
- Declaring the function "done" without testing it against expected output
  for a few different inputs.
- Not planning the function's logic (in comments) before writing code — this
  leads to drifting away from what the function was actually supposed to do.
