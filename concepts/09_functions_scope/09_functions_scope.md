# Functions — Scope

## What it is
Scope determines where in your code a variable can be seen and used.

## Local scope
Variables created *inside* a function only exist inside that function.
They disappear once the function finishes running.

```python
def my_function():
    x = 10   # local variable
    print(x)

my_function()
print(x)   # NameError! x doesn't exist outside the function
```

## Global scope
Variables created outside any function are global — they can be *read*
from inside functions, but not changed, unless you use the `global` keyword.

```python
count = 0

def increment():
    print(count)   # this works fine (reading)

def broken_increment():
    count += 1     # UnboundLocalError! Python treats count as local here

def fixed_increment():
    global count
    count += 1     # now it modifies the global variable
```

## Why this matters
Keeping variables local (passing values in as parameters, returning
results out) makes functions predictable and easier to debug — this is
generally better practice than relying on `global`.

## Common pitfalls
- Assuming a variable defined inside a function will exist outside it —
  it won't.
- Trying to modify a global variable inside a function without the `global`
  keyword, causing an `UnboundLocalError`.
- Shadowing: naming a local variable the same as a global one, causing
  confusion about which one is being used inside the function.
