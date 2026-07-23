# Function Composition

## What it is
Function composition means building larger functionality by having one
function call another — breaking a big problem into small, reusable pieces
rather than writing one giant function that does everything.

## Example
```python
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def describe_temperature(c):
    f = celsius_to_fahrenheit(c)   # composing: reusing the first function
    if f > 85:
        return f"{f}°F — Hot"
    elif f > 60:
        return f"{f}°F — Mild"
    else:
        return f"{f}°F — Cold"

print(describe_temperature(30))
```

`describe_temperature` doesn't need to know *how* Celsius converts to
Fahrenheit — it just trusts `celsius_to_fahrenheit` to handle that piece.

## Why it matters
- Each function does one clear job (easier to test and debug individually)
- Reduces duplicated logic — fix a bug in one place, not scattered everywhere
- Makes code more readable: function names describe *what* is happening at
  a high level, hiding the *how* underneath

## Common pitfalls
- Writing one massive function that tries to do everything, instead of
  splitting responsibilities across smaller functions.
- Not testing the smaller "building block" functions on their own before
  combining them — bugs are much harder to trace once they're composed
  together.
