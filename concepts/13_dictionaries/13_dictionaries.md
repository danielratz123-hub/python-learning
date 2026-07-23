# Dictionaries

## What it is
A dictionary stores data as key-value pairs. Unlike lists (indexed by
position), dictionaries are indexed by a unique key you choose.

```python
person = {
    "name": "Joe",
    "age": 22,
    "job": "Mechanic"
}
```

## Accessing values
```python
person["name"]          # "Joe"
person.get("name")       # "Joe" -- safer, returns None instead of erroring
person.get("email", "N/A")  # "N/A" -- default value if key doesn't exist
```

## Adding / updating / removing
```python
person["email"] = "joe@example.com"   # add a new key
person["age"] = 23                     # update existing key
del person["job"]                       # remove a key
person.pop("email")                     # remove and return the value
```

## Looping through a dictionary
```python
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(key, value)

for value in person.values():
    print(value)

for key in person.keys():
    print(key)
```

## Checking membership
```python
"name" in person        # True (checks keys, not values)
```

## Common pitfalls
- Accessing a missing key with `person["missing"]` raises a `KeyError` —
  use `.get()` when the key might not exist.
- Keys must be unique — assigning to an existing key overwrites it rather
  than adding a duplicate.
- Confusing `.keys()`, `.values()`, and `.items()` — remember `.items()`
  gives you both key and value together, which is usually what you want
  in a loop.
