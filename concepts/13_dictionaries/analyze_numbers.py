# analyze_numbers.py
# Analyzes a list of numbers: sum, average, positive/negative counts
# Concepts: guard clause for edge cases, building multi-value dictionary, efficient calculation outside loop
# Written during Python learning journey

def analyze_numbers(number_list):
    if len(number_list) == 0:
        return None

    number_dict = {}
    positive_count = 0
    negative_count = 0

    number_dict["sum"] = sum(number_list)
    number_dict["average"] = sum(number_list) / len(number_list)

    for n in number_list:
        if n < 0:
            negative_count += 1
        else:
            positive_count += 1

    number_dict["positive_count"] = positive_count
    number_dict["negative_count"] = negative_count

    return number_dict

print(analyze_numbers([10, -5, 20, -3, 15]))
# {'sum': 37, 'average': 7.4, 'positive_count': 3, 'negative_count': 2}

print(analyze_numbers([4, 8, 12, 16]))
# {'sum': 40, 'average': 10.0, 'positive_count': 4, 'negative_count': 0}

print(analyze_numbers([-1, -2, -3]))
# {'sum': -6, 'average': -2.0, 'positive_count': 0, 'negative_count': 3}

print(analyze_numbers([]))
# None
