grades = [] # edited from laptop - magic test
gaa= 0

while True:
    grade = input("Add a grade (or 'done' to finish): ")

    if grade == "done":
        break
   
    grade = int(grade)

    if grade <0 or grade > 100:         
        print("invalid number choose a number beetwin 0 and 100")
        continue
    

    grades.append(grade)

print("\nYour grades:")

average_grade= round(sum(grades)/len(grades), 2)

for grade in grades:
    print(f"- {grade}")
    if grade > average_grade:
        gaa+=1

print(f"\nTotal grades: {(len(grades))}")
print("the average grade is:",average_grade)
print("the highest grade is: ",max(grades))
print("the lowest grade is: ",min(grades))
print("grades above average:",gaa)