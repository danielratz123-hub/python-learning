# Python Day 1 Test #2

**Student:** Daniel  
**Topic:** Python Fundamentals (Day 1) - Retake  
**Total Points:** 100

---

## Rules

1. No looking at old code
2. No Googling, no AI, no autocomplete tricks
3. If you don't know, write "I don't know" - that's a valid answer
4. Take your time. Quality over speed.

---

## Part 1: Concept Questions (25 points)

**Q1 (3 pts):** What does the `in` keyword do? Give an example.

**Q2 (3 pts):** What's the difference between `5 + 3` and `"5" + "3"`?

**Q3 (4 pts):** Explain what's wrong with this line and why:
```python
score + 10
```

**Q4 (3 pts):** What does `range(0, 10, 3)` produce? List all the values.

**Q5 (3 pts):** What's the difference between `break` and `continue`? Be specific.

**Q6 (3 pts):** What's the purpose of `.append()` and what does it work on?

**Q7 (3 pts):** Explain what's wrong with this code structurally:
```python
total = 0
for i in range(5):
    total += i
    print(total)
```
(Hint: the code runs, but doesn't do what most people want)

**Q8 (3 pts):** What does this print, and why?
```python
x = "hello"
print(x * 3)
```

---

## Part 2: Predict the Output (25 points)

**Q9 (4 pts):**
```python
a = 10
b = 4
print(a + b)
print(a % b)
print(a // b)
```
(Note: `//` is integer division - it divides and throws away the decimal)

**Q10 (5 pts):**
```python
total = 0
for i in range(2, 8):
    total += 1
print(total)
```

**Q11 (5 pts):**
```python
word = "python"
result = ""
for letter in word:
    if letter in "py":
        result += letter
print(result)
```

**Q12 (5 pts):**
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

**Q13 (6 pts):**
```python
x = 2
for i in range(4):
    x = x + i
print(x)
```

---

## Part 3: Find the Bug (20 points)

For each, identify the bug(s) AND provide the fix.

**Q14 (5 pts):**
```python
count = input("How many? ")
for i in range(count):
    print(i)
```

**Q15 (5 pts):**
```python
total = 0
numbers = [10, 20, 30]
for n in numbers:
    total = n
print(total)
```

**Q16 (5 pts):**
```python
word = input("Enter a word: ")
vowels = 0
for letter in word:
    if letter == "a" or "e" or "i":
        vowels += 1
print(vowels)
```

**Q17 (5 pts):**
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

---

## Part 4: Write Code From Scratch (30 points)

**Q18 (10 pts): Sum of Multiples**

Write a program that prints the sum of all multiples of 5 between 1 and 50 (so: 5 + 10 + 15 + 20 + 25 + 30 + 35 + 40 + 45 + 50).

Print just the final total.

---

**Q19 (10 pts): Count Specific Letter**

Write a program that:
- Asks the user for a word
- Asks the user for a single letter
- Counts how many times that letter appears in the word
- Prints something like: `The letter 'l' appears 3 times in 'hello world'`

---

**Q20 (10 pts): Smart Grade Calculator**

Write a program that:
- Asks the user how many grades they want to enter
- Loops that many times, getting each grade (must validate that each grade is between 0 and 100 - if not, ask again)
- After all grades are entered, prints:
  - The average (rounded to 2 decimals)
  - How many grades are passing (60 or above)
  - How many grades are failing (below 60)

---

**End of test.**

## Topics Covered in This Test

- Variables and types (int, float, string)
- Type conversion (int(), float(), str())
- Operators (+, -, *, /, %, //, **, ==, !=, <, >, <=, >=)
- Logical operators (and, or)
- The `in` keyword
- Conditionals (if, elif, else)
- Loops (for, while)
- Loop control (break, continue)
- range() function (including step parameter)
- f-strings
- Lists (creation, indexing, append, looping)
- Built-in functions (len, sum, max, min, round, input, print)
- String indexing and iteration
- The accumulator pattern
- The counter pattern
- Input validation
