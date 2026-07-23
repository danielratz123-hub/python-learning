# Lists

## What it is
A list is an ordered, changeable collection of items. It can hold mixed types,
though usually you'll keep one type per list.

```python
numbers = [1, 2, 3, 4, 5]
names = ["Joe", "Dana", "Amit"]
mixed = [1, "two", 3.0, True]
```

## Indexing
```python
names[0]     # "Joe"       (first item)
names[-1]    # "Amit"      (last item)
names[1:3]   # ["Dana", "Amit"]  (slice)
```

## Common list operations
```python
names.append("Noa")     # add to the end
names.insert(1, "Tal")  # insert at a specific position
names.remove("Dana")    # remove by value
names.pop()             # remove and return the last item
names.pop(0)            # remove and return item at index 0
len(names)               # number of items
names.sort()             # sort in place
sorted(names)             # returns a new sorted list, leaves original unchanged
names.reverse()          # reverse in place
```

## Checking membership
```python
"Joe" in names        # True/False
"Joe" not in names     # True/False
```

## Looping through a list
```python
for name in names:
    print(name)

for index, name in enumerate(names):
    print(index, name)
```

## Common pitfalls
- Index errors: accessing `names[10]` when the list only has 5 items raises
  an `IndexError`.
- `remove()` deletes by *value*, `pop()` deletes by *index* — mixing these up
  is a common mistake.
- Lists are mutable — if you assign `list_b = list_a`, both names point to the
  *same* list. Changing one changes the other. Use `list_a.copy()` or
  `list(list_a)` to make an independent copy.
