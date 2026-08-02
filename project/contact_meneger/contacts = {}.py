contacts = {}
def menu():
    while True:
        print("=== contact manager ===")
        print(F"you have{len(contacts)} contacts")
        print("choose an option by presing a number or press cancel to return to the manu: ")
        print("1.Add contact")
        print("2.Remove contact")
        print("3.Show the list")
        print("4.Search of contact")
        print("5.Edit a contact")
        print("6.exit")

        choise = input("Choose a number: ")

        if choise == "1":
            print("Add the contact nuber")
        elif choise == "2":
            print("Remove the contact here")
        elif choise == "3":
            print("showing the list")
        elif choise == "4":
            print("search for the contact")
        elif choise == "5":
            print("Edit the contact")
        elif choise == "6":
            break
        else:
            print("invalid choise try again")      

                               
menu()