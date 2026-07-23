# filter_by_category.py
# Filters a dictionary of prices, keeping items at or below a max price
# Concepts: dictionary filtering, building new dictionary from filtered items
# Written during Python learning journey

def filter_by_category(items, price):
    result = {}
    for name in items:
        if items[name] <= price:
            result[name] = items[name]
    return result

prices = {"apple": 3, "steak": 25, "bread": 5, "cheese": 15, "milk": 4}

cheap = filter_by_category(prices, 10)
print(cheap)    # {'apple': 3, 'bread': 5, 'milk': 4}

luxury = filter_by_category(prices, 100)
print(luxury)   # {'apple': 3, 'steak': 25, 'bread': 5, 'cheese': 15, 'milk': 4}

nothing = filter_by_category(prices, 2)
print(nothing)  # {}
