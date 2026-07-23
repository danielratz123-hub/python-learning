# Functions — Multiple Return Values

## What it is
A Python function can return more than one value at once. Under the hood,
Python packages them into a tuple.

## Syntax
```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

low, high = get_min_max([4, 8, 1, 9, 3])
print(low, high)   # 1 9
```

## What's actually happening
```python
result = get_min_max([4, 8, 1, 9, 3])
print(result)          # (1, 9)  -- it's a tuple
print(type(result))     # <class 'tuple'>
```

You can unpack it into separate variables (like above), or keep it as a
single tuple and access by index (`result[0]`, `result[1]`).

## Practical example
```python
def analyze_grades(grades):
    average = sum(grades) / len(grades)
    passed = average >= 60
    return average, passed

avg, did_pass = analyze_grades([70, 85, 60, 90])
```

## Common pitfalls
- Forgetting to unpack into the right *number* of variables — if the
  function returns 2 values but you only assign 1 variable, you'll get
  the whole tuple instead of just the first value (not an error, but often
  not what you intended).
- Confusing "returning multiple values" with "returning a list" — they
  behave similarly when unpacking, but they are different types
  (`tuple` vs `list`).
