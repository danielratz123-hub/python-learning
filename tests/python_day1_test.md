# Python Day 1 Test

**Student:** Daniel  
**Topic:** Python Fundamentals (Day 1)  
**Total Points:** 100

---

## Rules

1. No looking at old code
2. No Googling, no AI, no autocomplete tricks
3. If you don't know, write "I don't know" - that's a valid answer
4. Take your time. This isn't timed. Quality over speed.

---

## Part 1: Concept Questions (25 points)

Answer in your own words. Short answers are fine.

**Q1 (3 pts):** What's the difference between `=` and `==`?

**Q2 (3 pts):** What does the `%` operator do? Give an example.

**Q3 (3 pts):** What does `input()` always return, regardless of what the user types?

**Q4 (3 pts):** What's the difference between `break` and `continue` inside a loop?

**Q5 (3 pts):** What's the difference between a `for` loop and a `while` loop? When would you use each?

**Q6 (4 pts):** Explain what an f-string is and write an example using a variable inside one.

**Q7 (3 pts):** What does `range(2, 10, 2)` produce? List all the values.

**Q8 (3 pts):** What does this code do, and why is it a bug?
```python
count = 0
while count < 5:
    print(count)
```

---

## Part 2: Predict the Output (25 points)

For each snippet, write what it prints. Don't run the code - work it out in your head.

**Q9 (4 pts):**
```python
x = 5
y = "5"
print(x == y)
print(x + 3)
```

**Q10 (5 pts):**
```python
total = 0
for i in range(1, 6):
    total += i
print(total)
```

**Q11 (5 pts):**
```python
word = "hello"
result = ""
for i in range(len(word) - 1, -1, -1):
    result += word[i]
print(result)
```

**Q12 (5 pts):**
```python
numbers = [10, 20, 30, 40, 50]
count = 0
for n in numbers:
    if n > 25:
        count += 1
print(count)
```

**Q13 (6 pts):**
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

---

## Part 3: Find the Bug (20 points)

Each snippet has at least one bug. Tell me what's wrong AND how to fix it.

**Q14 (5 pts):**
```python
age = input("How old are you? ")
if age >= 18:
    print("You're an adult")
```

**Q15 (5 pts):**
```python
total = 0
numbers = [10, 20, 30]
for n in numbers:
    total + n
print(total)
```

**Q16 (5 pts):**
```python
i = 0
while i < 5:
    print(i)
i += 1
```

**Q17 (5 pts):**
```python
grade = int(input("Enter grade: "))
if grade < 0 and grade > 100:
    print("Invalid")
else:
    print("Valid")
```

---

## Part 4: Write Code From Scratch (30 points)

Write actual working code for these. Open a new file in VS Code, but don't reference your old code.

**Q18 (10 pts): Temperature Converter**

Write a program that:
- Asks the user for a temperature in Celsius
- Converts it to Fahrenheit (formula: `F = C * 9/5 + 32`)
- Prints the result with 2 decimal places, like: `25.0°C = 77.00°F`

**Q19 (10 pts): Count Vowels**

Write a program that:
- Asks the user for a word
- Counts how many vowels (a, e, i, o, u) it contains
- Prints something like: `The word 'hello' contains 2 vowels`

Hint: you can check if a letter is a vowel with `if letter in "aeiou":`

**Q20 (10 pts): Simple Statistics**

Write a program that:
- Asks the user for 5 numbers (one at a time)
- Stores them in a list
- Prints: the sum, the average (rounded to 2 decimals), and the largest number
- Then prints how many of the numbers are larger than the average

---

**End of test.**

## Topics Covered in This Test

- Variables and types (int, float, string)
- Type conversion (int(), float(), str())
- Operators (+, -, *, /, %, **, ==, !=, <, >, <=, >=)
- Logical operators (and, or)
- Conditionals (if, elif, else)
- Loops (for, while)
- Loop control (break, continue)
- range() function
- f-strings
- Lists (creation, indexing, append, looping)
- Built-in functions (len, sum, max, min, round, input, print)
- String indexing
- The accumulator pattern
- Reading and understanding error messages
