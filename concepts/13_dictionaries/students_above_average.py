# students_above_average.py
# Filters students whose score is above the class average
# Concepts: dictionary iteration, calculating average, filtering by condition
# Written during Python learning journey

def students_above_average(scores):
    score_list = []
    above_average_list = []
    for name in scores:
        score_list.append(scores[name])
    average_score = sum(score_list) / len(score_list)

    for name in scores:
        if scores[name] > average_score:
            above_average_list.append(name)

    return above_average_list

grades = {"Daniel": 85, "Sarah": 92, "Yossi": 78, "Rachel": 65, "Amir": 90}
result = students_above_average(grades)
print(result)
# ['Daniel', 'Sarah', 'Amir']
