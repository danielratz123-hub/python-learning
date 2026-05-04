# Python Day 1 Test - Correct Answers

**Topic:** Python Fundamentals (Day 1)  
**Total Points:** 100

---

## Part 1: Concept Questions (25 points)

### Q1 (3 pts): Difference between `=` and `==`

`=` is the **assignment operator** - it gives a value to a variable.
```python
x = 5  # assigns 5 to x
```

`==` is the **comparison operator** - it checks if two values are equal and returns True or False.
```python
if x == 5:  # checks if x equals 5
```

---

### Q2 (3 pts): What does the `%` operator do?

The `%` operator (called **modulo**) returns the **remainder** of a division.

Examples:
- `7 % 3 = 1` (because 7 ÷ 3 = 2 with remainder 1)
- `10 % 2 = 0` (because 10 ÷ 2 = 5 with remainder 0)
- `15 % 4 = 3` (because 15 ÷ 4 = 3 with remainder 3)

Common use: checking if a number is even (`number % 2 == 0`) or odd (`number % 2 != 0`).

---

### Q3 (3 pts): What does input() always return?

`input()` always returns a **string**, no matter what the user types - even if they type numbers.

```python
age = input("How old are you? ")  # If user types 25, age = "25" (string, not int)
```

To use it as a number, convert it: `age = int(input("..."))`

---

### Q4 (3 pts): Difference between `break` and `continue`

- `break` - **exits the loop entirely**. The loop stops and code after the loop runs.
- `continue` - **skips the rest of the current iteration** and goes back to the TOP of the loop for the next iteration.

```python
for i in range(5):
    if i == 3:
        break  # loop stops completely when i reaches 3
    print(i)  # prints 0, 1, 2

for i in range(5):
    if i == 3:
        continue  # skips printing 3, but continues looping
    print(i)  # prints 0, 1, 2, 4
```

---

### Q5 (3 pts): Difference between `for` and `while` loops

- **`for` loop**: iterates over a known sequence (range, list, string). Use when you know what you're looping through.
- **`while` loop**: continues as long as a condition is True. Use when you don't know how many iterations you need.

```python
# for - I know I want 5 iterations
for i in range(5):
    print(i)

# while - keep asking until valid input (unknown number of tries)
while True:
    answer = input("Type 'yes': ")
    if answer == "yes":
        break
```

---

### Q6 (4 pts): What is an f-string?

An **f-string** (formatted string literal) is a special type of string in Python prefixed with `f`. It allows you to embed variables and expressions inside `{}` directly in the string.

```python
name = "Daniel"
age = 22
print(f"My name is {name} and I'm {age} years old")
# Output: My name is Daniel and I'm 22 years old

# Can also do calculations inside:
print(f"In 10 years I'll be {age + 10}")
```

---

### Q7 (3 pts): What does `range(2, 10, 2)` produce?

It produces: **2, 4, 6, 8**

**IMPORTANT:** `range(start, stop, step)` STOPS BEFORE `stop`. The end value is **exclusive** - it never includes the `stop` number.

So `range(2, 10, 2)` starts at 2, jumps by 2, and stops before reaching 10.

---

### Q8 (3 pts): What's the bug in this code?

```python
count = 0
while count < 5:
    print(count)
```

**Bug:** This is an **infinite loop**. The variable `count` never changes inside the loop, so `count < 5` is always True. The loop will print 0 forever.

**Fix:** Add `count += 1` inside the loop:
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

---

## Part 2: Predict the Output (25 points)

### Q9 (4 pts):
```python
x = 5
y = "5"
print(x == y)
print(x + 3)
```

**Output:**
```
False
8
```

**Why:** `x` is the integer 5, `y` is the string "5". They are different types, so `x == y` is False. The second line `x + 3` = 5 + 3 = 8.

---

### Q10 (5 pts):
```python
total = 0
for i in range(1, 6):
    total += i
print(total)
```

**Output:** `15`

**Why:** `range(1, 6)` produces 1, 2, 3, 4, 5 (NOT 6 - exclusive end!). Sum: 1+2+3+4+5 = 15.

---

### Q11 (5 pts):
```python
word = "hello"
result = ""
for i in range(len(word) - 1, -1, -1):
    result += word[i]
print(result)
```

**Output:** `olleh`

**Why:** `len(word) - 1` is 4 (last index). `range(4, -1, -1)` produces 4, 3, 2, 1, 0. So we get `word[4]`+`word[3]`+`word[2]`+`word[1]`+`word[0]` = "o"+"l"+"l"+"e"+"h" = "olleh".

---

### Q12 (5 pts):
```python
numbers = [10, 20, 30, 40, 50]
count = 0
for n in numbers:
    if n > 25:
        count += 1
print(count)
```

**Output:** `3`

**Why:** Numbers greater than 25 are 30, 40, 50 - that's 3 numbers.

---

### Q13 (6 pts):
```python
x = 10
if x > 5:
    if x > 15:
        print("A")
    else:
        print("B")
else:
    print("C")
```

**Output:** `B`

**Why:** x=10 is greater than 5, so we enter the first if. x=10 is NOT greater than 15, so we enter the inner else and print "B".

---

## Part 3: Find the Bug (20 points)

### Q14 (5 pts):
```python
age = input("How old are you? ")
if age >= 18:
    print("You're an adult")
```

**Bug:** `input()` returns a string. Comparing a string with `>= 18` (integer) causes a TypeError.

**Fix:**
```python
age = int(input("How old are you? "))
if age >= 18:
    print("You're an adult")
```

---

### Q15 (5 pts):
```python
total = 0
numbers = [10, 20, 30]
for n in numbers:
    total + n
print(total)
```

**Bug:** `total + n` calculates a value but doesn't store it anywhere. `total` stays at 0.

**Fix:** Use `total += n` (or `total = total + n`):
```python
total = 0
numbers = [10, 20, 30]
for n in numbers:
    total += n
print(total)
```

---

### Q16 (5 pts):
```python
i = 0
while i < 5:
    print(i)
i += 1
```

**Bug:** `i += 1` is OUTSIDE the while loop (wrong indentation). This causes an infinite loop because `i` never increases inside the loop.

**Fix:** Indent `i += 1` so it's inside the loop:
```python
i = 0
while i < 5:
    print(i)
    i += 1
```

---

### Q17 (5 pts):
```python
grade = int(input("Enter grade: "))
if grade < 0 and grade > 100:
    print("Invalid")
else:
    print("Valid")
```

**Bug:** Using `and` means the grade must be BOTH less than 0 AND greater than 100, which is impossible.

**Fix:** Use `or`:
```python
grade = int(input("Enter grade: "))
if grade < 0 or grade > 100:
    print("Invalid")
else:
    print("Valid")
```

---

## Part 4: Write Code From Scratch (30 points)

### Q18 (10 pts): Temperature Converter

```python
C = float(input("Enter the temperature in Celsius: "))
F = C * 9/5 + 32
print(f"{C}°C = {round(F, 2)}°F")
```

**Example output:** `25.0°C = 77.0°F`

---

### Q19 (10 pts): Count Vowels

```python
word = input("Enter a word: ")
vowel_count = 0

for letter in word:
    if letter in "aeiou":
        vowel_count += 1

print(f"The word '{word}' contains {vowel_count} vowels")
```

**Example output:** `The word 'hello' contains 2 vowels`

---

### Q20 (10 pts): Simple Statistics

```python
numbers = []

for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

total = sum(numbers)
average = round(total / len(numbers), 2)
largest = max(numbers)

count_above_average = 0
for num in numbers:
    if num > average:
        count_above_average += 1

print(f"Sum: {total}")
print(f"Average: {average}")
print(f"Largest: {largest}")
print(f"Numbers above average: {count_above_average}")
```

---

## Key Concepts to Remember

1. **`range(start, stop, step)`** - stop is EXCLUSIVE (never reached)
2. **`input()`** - always returns a string, must convert with `int()` or `float()` for math
3. **Type matters** - `5` and `"5"` are NOT equal
4. **`+=` vs `+`** - `+` calculates, `+=` calculates AND stores
5. **`and` vs `or`** - `and` requires BOTH true, `or` requires AT LEAST ONE true
6. **Indentation defines blocks** - wrong indentation = wrong logic
7. **`break` exits loop** - `continue` skips to next iteration
