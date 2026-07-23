def calculate(a, b):
    total = a + b
    return total      # function ends, total disappears

x = 5
y = 10
result = calculate(x, y)    # result = 15
print(result)                # CRASH - 'total' doesn't exist out here