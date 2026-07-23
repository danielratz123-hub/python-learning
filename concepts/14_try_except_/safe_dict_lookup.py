# safe_dict_lookup.py
# Safely looks up a key in a dictionary, returning a message on failure
# Concepts: try/except with KeyError, safe defaults
# Written during Python learning journey

def safe_dict_lookup(dict, key):
    try:
        return dict[key]
    except KeyError:
        return "Key not found"

prices = {"apple": 3, "bread": 5, "milk": 4}

print(safe_dict_lookup(prices, "apple"))     # 3
print(safe_dict_lookup(prices, "milk"))      # 4
print(safe_dict_lookup(prices, "banana"))    # Key not found
print(safe_dict_lookup(prices, "cheese"))    # Key not found
