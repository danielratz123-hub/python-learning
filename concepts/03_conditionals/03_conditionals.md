# Conditionals (if / elif / else)

## What it is
Conditionals let your program make decisions and run different code
depending on whether something is True or False.

## Basic syntax
```python
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```

- `if` — checked first
- `elif` — checked only if the previous conditions were False (can have many)
- `else` — runs only if nothing above matched

## Indentation matters
Python uses indentation (not curly braces) to define which code belongs to
which block. Inconsistent indentation causes errors.

## Combining conditions
```python
if age >= 18 and has_license:
    print("Can drive")

if is_weekend or is_holiday:
    print("No work today")
```

## Truthy and falsy values
Some values act like `False` even though they aren't the boolean `False`:
- `0`, `0.0` → falsy
- `""` (empty string) → falsy
- `[]`, `{}` (empty list/dict) → falsy
- Anything else (non-zero numbers, non-empty strings/lists) → truthy

```python
name = ""
if name:
    print("Has a name")
else:
    print("Name is empty")  # this runs
```

## Common pitfalls
- Using `=` instead of `==` (assignment vs comparison) — `=` inside an `if`
  is a syntax error in Python, so this one usually gets caught immediately.
- Forgetting that `elif` short-circuits — once one condition matches, the
  rest are skipped, even if they'd also be True.
