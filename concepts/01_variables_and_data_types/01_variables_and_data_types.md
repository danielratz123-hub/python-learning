# Variables and Data Types

## What it is
A variable is a name that points to a value stored in memory. Python figures out
the data type automatically based on what you assign — this is called "dynamic typing."

## Core data types
- `int` — whole numbers: `age = 22`
- `float` — decimal numbers: `price = 19.99`
- `str` — text: `name = "Joe"`
- `bool` — True/False: `is_active = True`

## Declaring variables
```python
age = 22
name = "Joe"
is_mechanic = True
```

No need to declare a type ahead of time — the value determines it.

## Checking a type
```python
type(age)   # <class 'int'>
type(name)  # <class 'str'>
```

## Type conversion (casting)
```python
str(22)      # "22"
int("22")    # 22
float("3.5") # 3.5
```

## Common pitfalls
- Mixing types without converting: `"Age: " + 22` throws a `TypeError`. Use
  `"Age: " + str(22)` or an f-string instead.
- Typos in variable names create a *new* variable instead of raising an error
  immediately — this only surfaces later as a `NameError` when you try to use
  the correctly-spelled one. Double-check spelling (a recurring issue: `lenght`,
  `hight`, `counrty`, etc.)

## Naming rules
- Must start with a letter or underscore
- Case-sensitive (`Age` and `age` are different variables)
- Use `snake_case` by convention (`first_name`, not `firstName`)
