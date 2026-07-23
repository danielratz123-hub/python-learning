# calculate_average.py
# Safely calculates an average, handling empty lists and bad data types
# Concepts: multiple exceptions in one except, edge case handling
# Written during Python learning journey

def calculate_average(numbers):
    try:
        return sum(numbers) / len(numbers)
    except (ZeroDivisionError, TypeError):
        return None

print(calculate_average([10, 20, 30, 40]))         # 25.0
print(calculate_average([5, 15, 25]))              # 15.0
print(calculate_average([]))                       # None
print(calculate_average([10, "hello", 20]))        # None
print(calculate_average([100]))                    # 100.0
