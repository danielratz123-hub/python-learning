# merge_grades.py
# Merges two grade dictionaries, keeping the higher score per student
# Concepts: multiple dictionary parameters, conditional dictionary building, comparing values
# Written during Python learning journey

def merge_grades(dict_1, dict_2):
    result = {}
    for student in dict_1:
        result[student] = dict_1[student]
    for student in dict_2:
        if student in result:
            if dict_2[student] > result[student]:
                result[student] = dict_2[student]
        else:
            result[student] = dict_2[student]
    return result

math = {"Daniel": 85, "Sarah": 92, "Yossi": 78}
english = {"Daniel": 90, "Sarah": 88, "Rachel": 95}

result = merge_grades(math, english)
print(result)
# {'Daniel': 90, 'Sarah': 92, 'Yossi': 78, 'Rachel': 95}
