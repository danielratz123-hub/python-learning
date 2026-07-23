# count_evens.py
# Counts how many even numbers are in a list
# Concepts: functions, parameters, return, loops, modulo, counter pattern
# Written during Python learning journey

def count_evens(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return count

result = count_evens([4, 2, 7, 5, 8, 12])
print(result)
# Output: 4
