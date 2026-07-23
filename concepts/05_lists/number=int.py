statistic = int
statistic = [statistic]
number = float

while True :
 if len(statistic) <= 5 :
  number1 = int(input("enter a number:"))

 else:
   print("done")
 break

print("the number are:",statistic)

print("the sum of the numbers are:",sum(statistic))

print("the average is:", sum(statistic)/len(number))



