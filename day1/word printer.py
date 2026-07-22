grades_list = []
passing = 0
failing = 0
while True:
 grade = (input("Enter a grade: "))
 
 if grade in "done" :
  break
 
 grade = int(grade)

 if grade >100 or grade < 0 :
  print("invalid grade plz try again.")
 
 else :
  grades_list.append(grade)
  
for i in grades_list :
 if i >= 60 :
  passing += 1
 else :
  failing +=1

  

average = round(sum(grades_list) / len(grades_list),3)
print(grades_list)  
print ("the average is ", average)
print("the passing grade number is:", passing)
print("the failing grade number is:", failing)