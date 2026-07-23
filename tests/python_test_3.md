# Python Test #3

**Student:** Daniel
**Date:** Session 19
**Format:** Same as Tests #1 and #2
**Previous scores:** Test #1: 43/100, Test #2: 74/100
**Goal:** 80%+

---

## Rules

- No hints during the test
- No looking at previous code files
- Take your time - accuracy > speed
- Write "I don't know" if you don't know - don't guess randomly
- Total: 100 points

---

## Section 1: Concept Questions (20 points, 4 each)

**Q1.** What's the difference between `/` and `//` in Python? Give an example.

**Q2.** What does `.split()` do to a string? Give an example.

**Q3.** What's the difference between `print()` and `return` inside a function?

**Q4.** What happens if you try to access a dictionary key that doesn't exist? What error do you get?

**Q5.** In a `try/except` block, when does the code inside `except` run?

---

## Section 2: Output Prediction (30 points, 5 each)

**Q6.** What does this print?
```python
x = 17
print(x // 5)
print(x % 5)
```

**Q7.** What does this print?
```python
result = 0
for i in range(1, 6):
    if i % 2 == 0:
        result += i
print(result)
```

**Q8.** What does this print?
```python
def transform(a, b=3):
    return a * b + 1

print(transform(4))
print(transform(4, 5))
```

**Q9.** What does this print?
```python
text = "hello world python"
words = text.split()
print(len(words))
print(words[1])
```

**Q10.** What does this print?
```python
scores = {"a": 10, "b": 25, "c": 15}
biggest_key = "a"
for key in scores:
    if scores[key] > scores[biggest_key]:
        biggest_key = key
print(biggest_key)
```

**Q11.** What does this print?
```python
def safe_convert(s):
    try:
        return int(s)
    except ValueError:
        return -1

print(safe_convert("42"))
print(safe_convert("hello"))
print(safe_convert("100"))
```

---

## Section 3: Bug Hunting (20 points, 5 each)

**Q12.** Find the bug:
```python
count = 0
words = ["hello", "hi", "hey"]
for w in words:
    count + 1
print(count)
```

**Q13.** Find the bug:
```python
def is_adult(age):
    if age >= 18:
        return "adult"
    return "minor"
    if age < 0:
        return "invalid"
```

**Q14.** Find the bug:
```python
def count_vowels(word):
    count = 0
    for letter in word:
        if letter == "a" or "e" or "i" or "o" or "u":
            count += 1
    return count

print(count_vowels("hello"))
```

**Q15.** Find the bug:
```python
def get_average(numbers):
    total = 0
    for n in numbers:
        total = n
    return total / len(numbers)

print(get_average([10, 20, 30]))
```

---

## Section 4: Code Writing (30 points, 15 each)

**Q16.** Write a function called `count_long_words` that:
- Takes TWO parameters: a list of words and a minimum length
- Returns the count of how many words are LONGER than the minimum length

Test cases (include these in your code):
```python
print(count_long_words(["cat", "elephant", "dog", "rhinoceros"], 4))
# Expected: 2 (elephant and rhinoceros)

print(count_long_words(["hi", "hello", "world"], 2))
# Expected: 2 (hello and world)

print(count_long_words(["a", "b", "c"], 5))
# Expected: 0
```

---

**Q17.** Write a function called `safe_grade_lookup` that:
- Takes TWO parameters: a dictionary of student grades AND a student name
- Returns the grade if the student exists
- Returns the string `"Student not found"` if the student doesn't exist
- Uses try/except (not `if in`)

Test cases (include these in your code):
```python
grades = {"Daniel": 85, "Sarah": 92, "Yossi": 78}

print(safe_grade_lookup(grades, "Daniel"))
# Expected: 85

print(safe_grade_lookup(grades, "Sarah"))
# Expected: 92

print(safe_grade_lookup(grades, "Rachel"))
# Expected: Student not found
```

---

## End of Test

Send your answers when done. You can send them all together or in sections.

For code writing questions, send screenshots of your VS Code + terminal output.
