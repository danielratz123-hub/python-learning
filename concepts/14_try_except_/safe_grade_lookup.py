# safe_grade_lookup.py
# Safely looks up a student's grade, from Test #3
# Concepts: try/except with KeyError, safe defaults
# Written during Python learning journey

def safe_grade_lookup(dict, name):
    try:
        return dict[name]
    except KeyError:
        return "Student not found"

grades = {"Daniel": 85, "Sarah": 92, "Yossi": 78}

print(safe_grade_lookup(grades, "Daniel"))    # 85
print(safe_grade_lookup(grades, "Sarah"))     # 92
print(safe_grade_lookup(grades, "Rachel"))    # Student not found
