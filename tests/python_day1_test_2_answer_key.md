# Python Day 1 Test #2 - Correct Answers

**Topic:** Python Fundamentals (Day 1) - Retake  
**Total Points:** 100

---

## Part 1: Concept Questions (25 points)

### Q1 (3 pts): What does the `in` keyword do?

`in` is a Python operator that has two uses:

**Use 1 - Membership check (returns True or False):**
```python
print("a" in "apple")     # True - "a" is in "apple"
print(5 in [1, 2, 3])     # False - 5 is not in this list
print("z" in "hello")     # False
```

**Use 2 - In a for loop, it specifies what to iterate over:**
```python
for letter in "hello":    # iterate over each character
    print(letter)

for num in [1, 2, 3]:     # iterate over each item
    print(num)
```

---

### Q2 (3 pts): Difference between `5 + 3` and `"5" + "3"`

- `5 + 3` = `8` (math addition between integers)
- `"5" + "3"` = `"53"` (string concatenation - joins text together)

The `+` operator behaves differently based on the types involved.

---

### Q3 (4 pts): What's wrong with `score + 10`?

The line calculates a value but **doesn't store it anywhere**. The result is thrown away. No error, no crash - just a wasted line of code.

To actually update score, you need:
```python
score += 10        # or
score = score + 10
```

This is one of the most common silent bugs - the program runs but does nothing useful.

---

### Q4 (3 pts): What does `range(0, 10, 3)` produce?

**Output: 0, 3, 6, 9**

Starts at 0, jumps by 3, stops BEFORE 10 (exclusive end).

---

### Q5 (3 pts): Difference between `break` and `continue`

- **`break`** - exits the loop entirely. The loop stops, and code AFTER the loop runs.
- **`continue`** - skips the rest of the current iteration and goes back to the TOP of the loop for the next iteration.

```python
for i in range(5):
    if i == 3:
        break          # stops at 3, loop ends completely
    print(i)
# Output: 0, 1, 2

for i in range(5):
    if i == 3:
        continue       # skips 3, but loop continues
    print(i)
# Output: 0, 1, 2, 4
```

---

### Q6 (3 pts): Purpose of `.append()`

`.append()` adds a single item to the END of a list. It works on lists only.

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)    # [1, 2, 3, 4]
```

---

### Q7 (3 pts): What's wrong structurally with this code?

```python
total = 0
for i in range(5):
    total += i
    print(total)
```

The `print(total)` is INSIDE the loop, so it prints 5 times (the running total at each step). Most programmers want to print only the FINAL total ONCE, after the loop ends.

Fix: move `print(total)` outside the loop (no indentation):
```python
total = 0
for i in range(5):
    total += i
print(total)        # prints once, after loop ends
```

---

### Q8 (3 pts): What does `print(x * 3)` print when x = "hello"?

**Output: `hellohellohello`**

In Python, `string * number` repeats the string. So `"hello" * 3` = `"hellohellohello"` (no spaces - just concatenated three times).

This works in either order: `3 * "hello"` produces the same result.

---

## Part 2: Predict the Output (25 points)

### Q9 (4 pts):
```python
a = 10
b = 4
print(a + b)        # 14
print(a % b)        # 2  (10 ÷ 4 = 2 remainder 2)
print(a // b)       # 2  (integer division - 10 ÷ 4 = 2, decimal thrown away)
```

**Output:**
```
14
2
2
```

---

### Q10 (5 pts):
```python
total = 0
for i in range(2, 8):
    total += 1
print(total)
```

**Output: 6**

`range(2, 8)` produces 2, 3, 4, 5, 6, 7 - that's **6 iterations**. Each iteration adds 1 to total (NOT i), so total ends at 6.

---

### Q11 (5 pts):
```python
word = "python"
result = ""
for letter in word:
    if letter in "py":
        result += letter
print(result)
```

**Output: `py`**

Only letters that are in "py" get added. From "python", only 'p' and 'y' qualify.

---

### Q12 (5 pts):
```python
numbers = [3, 8, 12, 5, 20]
total = 0
for n in numbers:
    if n > 10:
        total += n
    else:
        total -= n
print(total)
```

**Output: 16**

Trace:
- n=3: 3 > 10? No → total -= 3 → total = -3
- n=8: 8 > 10? No → total -= 8 → total = -11
- n=12: 12 > 10? Yes → total += 12 → total = 1
- n=5: 5 > 10? No → total -= 5 → total = -4
- n=20: 20 > 10? Yes → total += 20 → total = 16

---

### Q13 (6 pts):
```python
x = 2
for i in range(4):
    x = x + i
print(x)
```

**Output: 8**

Trace:
- Start: x = 2
- i=0: x = 2 + 0 = 2
- i=1: x = 2 + 1 = 3
- i=2: x = 3 + 2 = 5
- i=3: x = 5 + 3 = 8

---

## Part 3: Find the Bug (20 points)

### Q14 (5 pts):
```python
count = input("How many? ")
for i in range(count):
    print(i)
```

**Bug:** `count` is a string (input() returns string). `range()` requires an integer.

**Fix:**
```python
count = int(input("How many? "))
for i in range(count):
    print(i)
```

---

### Q15 (5 pts):
```python
total = 0
numbers = [10, 20, 30]
for n in numbers:
    total = n
print(total)
```

**Bug:** `total = n` overwrites total each iteration instead of adding to it. After the loop, total just equals the last value (30).

**Fix:** Use `+=`:
```python
total = 0
numbers = [10, 20, 30]
for n in numbers:
    total += n
print(total)        # 60
```

---

### Q16 (5 pts):
```python
word = input("Enter a word: ")
vowels = 0
for letter in word:
    if letter == "a" or "e" or "i":
        vowels += 1
print(vowels)
```

**Bug:** `letter == "a" or "e" or "i"` doesn't do what it looks like. Python reads it as three separate conditions: `(letter == "a")` OR `("e")` OR `("i")`. Since non-empty strings are "truthy", the condition is ALWAYS True, so every letter gets counted as a vowel.

**Fix:** Use `in` for clean syntax:
```python
if letter in "aei":
    vowels += 1
```

Or repeat the variable:
```python
if letter == "a" or letter == "e" or letter == "i":
    vowels += 1
```

---

### Q17 (5 pts):
```python
numbers = []
for i in range(5):
    n = int(input("Number: "))
    numbers.append(n)

average = sum(numbers) / len(numbers)
above = 0
for n in numbers:
    if n > average:
        above + 1
print(f"Above average: {above}")
```

**Bug:** `above + 1` calculates but doesn't store. `above` stays at 0 forever.

**Fix:** Use `+=`:
```python
if n > average:
    above += 1
```

---

## Part 4: Write Code From Scratch (30 points)

### Q18 (10 pts): Sum of Multiples

```python
total = 0
for n in range(5, 51, 5):
    total += n
print(total)
```

**Output: 275**

Note: Start at 5 (not 0) because the problem says "between 1 and 50". Use 51 as stop value to include 50.

---

### Q19 (10 pts): Count Specific Letter

```python
word = input("Enter a word: ")
letter_to_find = input("Enter a letter: ")
count = 0

for letter in word:
    if letter == letter_to_find:
        count += 1

print(f"The letter '{letter_to_find}' appears {count} times in '{word}'")
```

Key requirement: ASK the user for the letter to count - don't hardcode it.

---

### Q20 (10 pts): Smart Grade Calculator

```python
count = int(input("How many grades? "))
grades_list = []

for i in range(count):
    while True:
        grade = int(input(f"Enter grade {i+1}: "))
        if grade < 0 or grade > 100:
            print("Invalid grade. Must be between 0 and 100.")
        else:
            grades_list.append(grade)
            break

passing = 0
failing = 0
for grade in grades_list:
    if grade >= 60:
        passing += 1
    else:
        failing += 1

average = round(sum(grades_list) / len(grades_list), 2)

print(f"Average: {average}")
print(f"Passing: {passing}")
print(f"Failing: {failing}")
```

Notes:
- The exercise specified asking how MANY grades upfront (use `for` loop, not `while True` with a "done" exit)
- Use nested loop for validation - re-ask until valid
- Use `==` not `in` for exact string matches

---

## Key Concepts Tested

1. **`range(start, stop, step)`** - stop is EXCLUSIVE
2. **Type awareness** - `5 != "5"`, mixed types cause errors
3. **`+=` vs `+`** - calculation without assignment is wasted
4. **`%` (modulo)** - returns the remainder
5. **`//` (integer division)** - divides, throws away decimal
6. **`*` with strings** - repeats the string
7. **`in` operator** - membership check (True/False)
8. **`break` vs `continue`** - exit loop vs skip iteration
9. **List operations** - `.append()`, `sum()`, `len()`
10. **The accumulator pattern** - initialize, loop, accumulate, print result
11. **The counter pattern** - count things with `count += 1`
12. **Following specifications exactly** - read requirements twice
