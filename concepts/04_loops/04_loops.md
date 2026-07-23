# Loops (for / while)

## `for` loops
Used when you're iterating over a known sequence (a list, string, range, etc.)

```python
for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

for name in ["Joe", "Dana", "Amit"]:
    print(name)

for char in "hello":
    print(char)
```

`range(start, stop, step)`:
```python
range(5)          # 0,1,2,3,4
range(2, 6)       # 2,3,4,5
range(0, 10, 2)   # 0,2,4,6,8
```

## `while` loops
Used when you don't know in advance how many times you'll loop — it runs
as long as a condition stays True.

```python
count = 0
while count < 5:
    print(count)
    count += 1   # without this, infinite loop!
```

## `break` and `continue`
```python
for i in range(10):
    if i == 5:
        break       # exits the loop entirely
    if i % 2 == 0:
        continue    # skips to the next iteration
    print(i)
```

## Common pitfalls
- **Infinite loops**: forgetting to update the condition variable in a
  `while` loop (classic case of the `+=` vs `+` bug from the operators file).
- **Off-by-one errors**: `range(5)` gives you 0–4, not 1–5. If you need 1–5,
  use `range(1, 6)`.
- Mixing up `break` (stop the loop completely) with `continue` (skip just
  this iteration).
