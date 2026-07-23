# Operators

## Arithmetic operators
```python
+   # addition
-   # subtraction
*   # multiplication
/   # division (always returns a float)
//  # floor division (drops the remainder)
%   # modulo (remainder)
**  # exponent
```

Example:
```python
7 / 2   # 3.5
7 // 2  # 3
7 % 2   # 1
2 ** 3  # 8
```

## Comparison operators
```python
==  # equal to
!=  # not equal to
>   # greater than
<   # less than
>=  # greater than or equal to
<=  # less than or equal to
```
These always return a `bool` (`True`/`False`).

## Logical operators
```python
and   # both conditions must be True
or    # at least one condition must be True
not   # inverts a boolean
```

## Assignment operators
```python
x = 5
x += 1   # same as x = x + 1
x -= 1
x *= 2
x /= 2
```

## The `+=` vs `+` trap (a recurring bug)
`+=` **updates and stores** the variable. Plain `+` just **computes a value**
that gets thrown away unless you assign it somewhere.

```python
total = 0
total + 5     # computes 5, but total is still 0 — nothing was saved!
total += 5    # total is now 5 — correctly stored
```

This is one of the most common silent bugs — the code runs with no error,
but the value never updates. Always double check: am I storing this result,
or just calculating it and discarding it?
