# Strings and String Methods

## What it is
A string is a sequence of characters. Strings are immutable — methods that
"change" a string actually return a brand new string.

```python
name = "Joe"
```

## Common string methods
```python
name.upper()          # "JOE"
name.lower()          # "joe"
name.strip()          # removes leading/trailing whitespace
name.replace("o", "0") # "J0e"
name.split(",")        # splits into a list on the separator
"-".join(["a","b","c"]) # "a-b-c"
name.find("o")          # returns index of first match, or -1
len(name)               # length of the string
name.startswith("J")    # True
name.endswith("e")      # True
name.count("o")         # how many times "o" appears
```

## Indexing and slicing (same as lists)
```python
name[0]     # "J"
name[-1]    # "e"
name[0:2]   # "Jo"
```

## Concatenation
```python
first = "Joe"
last = "Cohen"
full = first + " " + last   # "Joe Cohen"
```

## Common pitfalls
- Strings are immutable — `name.upper()` doesn't change `name` itself, it
  returns a new string. You need `name = name.upper()` to actually keep it.
- Concatenating a string with a non-string raises a `TypeError`
  (`"Age: " + 22` fails — needs `str(22)` or an f-string).
- Variable name typos are especially easy in string-heavy code
  (e.g. `grettings` instead of `greetings`).
