while True:
    choice = int(input("Enter 0 for even numbers or 1 for odd numbers: "))
    if choice == 0 or choice == 1:
        break
    print("Invalid choice. Please choose 0 for even numbers or 1 for odd numbers.")
if choice == 0:
    for i in range (0,101,2):
        print((i))
elif choice == 1:
    for i in range (1,101,2):
        print((i)) 