# Test #3 - Answer Key

Complete answer key for Python Test #3.

---

## Section 1: Concept Questions

### Q1. Difference between `/` and `//`

`/` is regular division that returns a decimal (float). Example: `10 / 3 = 3.333...`

`//` is integer division that returns only the whole number part, dropping any decimal. Example: `10 // 3 = 3`

Note: `//` NEVER returns decimals, even when dividing decimal numbers.

---

### Q2. What does `.split()` do

`.split()` is a string method that breaks a string into a list of words, using whitespace as the separator.

Example:
```python
text = "hello world from python"
words = text.split()
# words = ['hello', 'world', 'from', 'python']
```

You can also split by other characters: `text.split(",")` splits by commas.

---

### Q3. Difference between `print()` and `return` inside a function

`print()` displays a value on the screen but does NOT send it back to the caller. The function that called it can't use what was printed.

`return` sends a value back to the caller so it can be used, stored, or passed to another function. The function ends when it hits a return.

Example:
```python
def with_print(x):
    print(x * 2)  # shows on screen, returns None

def with_return(x):
    return x * 2  # sends back the value

result = with_print(5)   # prints 10, result = None
result = with_return(5)  # nothing printed, result = 10
```

---

### Q4. Accessing a non-existent dictionary key

You get a `KeyError` exception. The program crashes unless you handle it with try/except or check with `in` first.

Example:
```python
d = {"a": 1}
print(d["b"])  # KeyError: 'b'

# Safe alternatives:
if "b" in d:
    print(d["b"])
# OR
try:
    print(d["b"])
except KeyError:
    print("not found")
```

---

### Q5. When does `except` code run

The code inside `except` runs ONLY when an error of the specified type occurs in the `try` block.

If no error happens, the `except` block is completely skipped.

If a DIFFERENT type of error happens (one not caught), the `except` still doesn't run, and the program crashes.

---

## Section 2: Output Prediction

### Q6.
```python
x = 17
print(x // 5)  # 3
print(x % 5)   # 2
```

17 divided by 5 is 3 with remainder 2.

---

### Q7.
```python
result = 0
for i in range(1, 6):
    if i % 2 == 0:
        result += i
print(result)  # 6
```

Range 1-5. Evens: 2, 4. Sum: 2+4 = 6.

---

### Q8.
```python
def transform(a, b=3):
    return a * b + 1

print(transform(4))       # 13
print(transform(4, 5))    # 21
```

- transform(4): 4 * 3 + 1 = 13 (uses default b=3)
- transform(4, 5): 4 * 5 + 1 = 21

---

### Q9.
```python
text = "hello world python"
words = text.split()
print(len(words))  # 3
print(words[1])    # world
```

Split gives ['hello', 'world', 'python']. Length is 3. Index 1 is "world" (indexing starts at 0).

---

### Q10.
```python
scores = {"a": 10, "b": 25, "c": 15}
biggest_key = "a"
for key in scores:
    if scores[key] > scores[biggest_key]:
        biggest_key = key
print(biggest_key)  # b
```

Comparison tracking. "b" has the highest value (25).

---

### Q11.
```python
def safe_convert(s):
    try:
        return int(s)
    except ValueError:
        return -1

print(safe_convert("42"))     # 42
print(safe_convert("hello"))  # -1
print(safe_convert("100"))    # 100
```

"hello" causes ValueError, returns -1. Numeric strings convert normally.

---

## Section 3: Bug Hunting

### Q12. The bug
```python
count = 0
words = ["hello", "hi", "hey"]
for w in words:
    count + 1      # BUG - doesn't store result
print(count)       # prints 0
```

**Fix:** Change `count + 1` to `count += 1` to actually store the incremented value.

---

### Q13. The bug
```python
def is_adult(age):
    if age >= 18:
        return "adult"
    return "minor"
    if age < 0:        # UNREACHABLE - after return above
        return "invalid"
```

The `if age < 0` check never runs because `return "minor"` exits the function first for any age below 18 (including negatives).

**Fix:** Put the negative check FIRST:
```python
def is_adult(age):
    if age < 0:
        return "invalid"
    if age >= 18:
        return "adult"
    return "minor"
```

---

### Q14. The bug
```python
def count_vowels(word):
    count = 0
    for letter in word:
        if letter == "a" or "e" or "i" or "o" or "u":
            count += 1
    return count
```

The condition `if letter == "a" or "e" or ...` is wrong. In Python, this evaluates as:
- `letter == "a"` (correct check)
- OR `"e"` (non-empty string, always truthy = True)
- So the whole condition is ALWAYS True

**Fix:** Use the `in` operator:
```python
if letter in "aeiou":
    count += 1
```

This checks if letter is any of those characters.

---

### Q15. The bug
```python
def get_average(numbers):
    total = 0
    for n in numbers:
        total = n     # BUG - overwrites instead of accumulating
    return total / len(numbers)
```

`total = n` REPLACES total with n each iteration. After the loop, total is just the LAST number.

**Fix:** Use `total += n` to accumulate:
```python
def get_average(numbers):
    total = 0
    for n in numbers:
        total += n     # accumulates
    return total / len(numbers)
```

---

## Section 4: Code Writing

### Q16. count_long_words

```python
def count_long_words(words, minimum):
    count = 0
    for w in words:
        if len(w) > minimum:
            count += 1
    return count

# Tests
print(count_long_words(["cat", "elephant", "dog", "rhinoceros"], 4))
# Expected: 2 (elephant and rhinoceros)

print(count_long_words(["hi", "hello", "world"], 2))
# Expected: 2 (hello and world)

print(count_long_words(["a", "b", "c"], 5))
# Expected: 0
```

**Key point:** Returns a COUNT (number), not a list. The function name says "count_" - that's the giveaway.

---

### Q17. safe_grade_lookup

```python
def safe_grade_lookup(grades_dict, name):
    try:
        return grades_dict[name]
    except KeyError:
        return "Student not found"

# Tests
grades = {"Daniel": 85, "Sarah": 92, "Yossi": 78}

print(safe_grade_lookup(grades, "Daniel"))    # 85
print(safe_grade_lookup(grades, "Sarah"))     # 92
print(safe_grade_lookup(grades, "Rachel"))    # Student not found
```

**Key point:** Uses try/except (not `if in`), catches KeyError specifically, returns safe default string.
