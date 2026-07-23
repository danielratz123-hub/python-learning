# F-Strings

## What it is
F-strings (formatted string literals) let you embed variables and
expressions directly inside a string. They're the modern, preferred way to
build strings in Python (over `+` concatenation or `.format()`).

## Basic syntax
Put an `f` right before the opening quote, and wrap variables in `{}`:

```python
name = "Joe"
age = 22
print(f"My name is {name} and I am {age} years old.")
# "My name is Joe and I am 22 years old."
```

## Expressions inside f-strings
You can put any expression inside the braces, not just variable names:
```python
print(f"Next year I'll be {age + 1}")
print(f"Uppercase name: {name.upper()}")
```

## Formatting numbers
```python
price = 19.999
print(f"Price: ${price:.2f}")   # "Price: $20.00" — rounds to 2 decimals
```

## Why f-strings beat `+` concatenation
```python
# Old, error-prone way — fails if age isn't a string
"Age: " + str(age)

# F-string way — handles the conversion automatically
f"Age: {age}"
```

## Common pitfalls
- Forgetting the `f` prefix — without it, `{name}` prints literally instead
  of being substituted.
- Using the wrong quote type inside vs. outside the f-string can cause
  syntax errors — keep outer and inner quotes different (e.g. outer `"`,
  inner `'`).
