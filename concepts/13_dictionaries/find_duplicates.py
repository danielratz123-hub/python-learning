# find_duplicates.py
# Finds duplicate items in a list
# Concepts: two-loop pattern (count then check), avoiding duplicate appending, edge cases
# Written during Python learning journey

def find_duplicates(lists):
    new_list = []
    dict_1 = {}

    for w in lists:
        if w in dict_1:
            dict_1[w] += 1
        else:
            dict_1[w] = 1

    for value in dict_1:
        if dict_1[value] > 1:
            new_list.append(value)

    return new_list

print(find_duplicates([1, 2, 3, 2, 4, 3, 5]))         # [2, 3]
print(find_duplicates(["a", "b", "c", "b", "d", "a"])) # ['b', 'a']
print(find_duplicates([1, 2, 3, 4, 5]))                # []
print(find_duplicates([]))                              # []
print(find_duplicates([1, 1, 1, 2, 2, 2]))             # [1, 2]
