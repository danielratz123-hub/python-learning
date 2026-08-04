contacts = {}

def is_cancelled(value):
    return value.strip().lower() == "cancel"

def get_input(message):
    value = input(message).strip()

    if is_cancelled(value):
        return None

    return value
def menu():
    while True:
        print("\n=== contact manager ===")
        print(F"you have { len(contacts)} contacts")
        print("choose an option by presing a number or press cancel to return to the manu: ")
        print("1.Add contact")
        print("2.Remove contact")
        print("3.Show the list")
        print("4.Search of contact")
        print("5.Edit a contact")
        print("6.exit")

        choice = input("Choose a number: ").strip()

        if choice == "1":
            add_contacts()
        elif choice == "2":
            print("Remove the contact here")
        elif choice == "3":
            show_contact_list()
        elif choice == "4":
            print("search for the contact")
        elif choice == "5":
            print("Edit the contact")
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("invalid choise try again")   

def add_contacts():
    name = get_input("Enter a contact name: ")
    if name is None:
        return
    phone = get_input("Enter a phone number: ")
    if phone is None:
        return
    email = get_input("Enter an email: ")
    if email is None:
        return
    city = get_input("Enter a city: ")
    if city is None:
        return
    category = get_input("Enter a categoty: ")
    if category is None:
        return

    contacts[name] = {
        "phone": phone,
        "email": email,
        "city": city,
        "category": category
    }
    print(f"contact {name} added successfully")

def show_contact_list():
    print("\n===== Contact List =====")

    if not contacts:
        print("The contact list is empty.")
        return

    for number, (name, info) in enumerate(contacts.items(), start=1):
        print(f"\nContact {number}")
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print(f"City: {info['city']}")
        print(f"Category: {info['category']}")
menu()