total = 0
start = int(input("Enter the minimum number: "))
end = int(input("Enter the maximum number: "))
print("1 = all numbers, 2 = even only, 3 = odd only")
choice = int(input("Enter your choice: "))

for i in range(start, end + 1):
    
    if choice == 1:
        total += i  
    elif choice == 2 and i % 2 == 0:
        total += i  
    elif choice == 3 and i % 2 != 0:
        total += i  

print(f"The sum is {total}")