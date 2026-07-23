# Try / Except Error Handling

## What it is
`try`/`except` lets your program handle errors gracefully instead of
crashing when something goes wrong.

## Basic syntax
```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ValueError:
    print("That wasn't a valid number.")
except ZeroDivisionError:
    print("Can't divide by zero.")
```

- Code in `try` runs first.
- If an error occurs, Python jumps straight to the matching `except` block.
- If no error occurs, the `except` blocks are skipped entirely.

## Catching multiple error types
```python
try:
    risky_operation()
except (ValueError, TypeError):
    print("Invalid value or type.")
```

## `else` and `finally`
```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error!")
else:
    print(f"Success: {result}")   # runs only if no exception occurred
finally:
    print("This always runs.")     # runs no matter what (cleanup code)
```

## Common built-in exceptions
- `ValueError` — wrong value type for an operation (e.g. `int("abc")`)
- `TypeError` — wrong type used in an operation (e.g. `"a" + 5`)
- `ZeroDivisionError` — dividing by zero
- `KeyError` — accessing a missing dictionary key
- `IndexError` — accessing a list index that doesn't exist

## Common pitfalls
- Using a bare `except:` (catches *everything*, including typos and bugs
  you actually want to see) — always catch specific exception types.
- Wrapping too much code in one `try` block, making it unclear which line
  actually caused the error.
- Using `try/except` to silently hide bugs instead of genuinely handling
  expected error cases.
