how_meny = int(input("how meny number do you want to enter: "))

number_list = []


for i in range(how_meny):
    number = float (input("enter a number"))
    number_list.append(number)

average =round( sum(number_list) / len(number_list), 2)
print(number_list)

print("the sum of the number are:",sum(number_list))

print("the average of the number are:", average )