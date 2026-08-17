contacts = {}

def is_cancelled(value):
    return value.strip().lower() == "cancel"

def get_input(message):
    value = input(message).strip().lower()

    if is_cancelled(value):
        return None

    return value
def yes_or_no(question):
        while True:
         answer = input(question)

         if answer.strip().lower() == "yes": 
          return True
         
         elif answer.strip().lower() == "no": 
          return False

         else:
          print("invalid choice try again")

def display_contacts(number,name,info):
   
   print(f"\nContact {number}")
   print(f"Name: {name}")
   print(f"Phone: {info['phone']}")
   print(f"Email: {info['email']}")
   print(f"City: {info['city']}")
   print(f"Category: {info['category']}")
   

            
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
            remove_contacts()
        elif choice == "3":
            show_contact_list()
        elif choice == "4":
            search_contacts()
        elif choice == "5":
            edit_contact()
        elif choice == "6":
         if not yes_or_no("Are you sure you want to exit the program? (yes/no): "):
          continue

         print("Goodbye.")
         break
        else:
         print("Invalid choice, try again.")  

def add_contacts():
    name = get_input("Enter a contact name: ")

    if name in contacts:
       if not yes_or_no("Contact already exists — do you want to overwrite? (yes/no)"):
           return

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


def remove_contacts():
   while True:
      name = get_input("Enter a contact name: ")
      if name is None:
              return

      if name in contacts:
        if not yes_or_no(F"Are you sure you want to remove {name} from the list? (yes/no)"):
         return
        del contacts[name]
        print(f"contact {name} removed successfully ")
        return
      else:
        print("contact not found try again:")


def show_contact_list():
    print("\n===== Contact List =====")

    if not contacts:
        print("The contact list is empty.")
        return

    for number, (name, info) in enumerate(contacts.items(), start=1):
      display_contacts(number,name,info)
def edit_contact():
     while True:
      edit = get_input("Enter a contact name:")
      if edit is None:
       return
      if edit in contacts:
         break
      else:
       print("contact not found try again ")

       
     while True:
        print(" choose a field to edit or cancel to return: ")
        print("1.name")
        print("2.phone")
        print("3.email")
        print("4.city")
        print("5.category")

        choice = get_input("enter a number: ")
        if choice is None:    
         return

        elif choice == "1":
          print(f"Current name: {edit}")   
          new_name = get_input("Enter a new name: ")          
          if new_name is None:              
             continue      
          if new_name == edit:                  
             print("That's already the name — no change made.")
             continue                      
          if new_name in contacts:
             if not yes_or_no("Contact already exists — do you want to overwrite? (yes/no)"):
               continue
          if yes_or_no("Save this change? (yes/no): "):
           contacts[new_name]=contacts[edit]
           del contacts[edit]
           edit = new_name
           print("name has successfully updated.")

        elif choice == "2":
          print(f"Current phone: {contacts[edit]['phone']}")   
          new_phone = get_input("Enter a new phone: ")          
          if new_phone is None:                                 
            continue
          if yes_or_no("Save this change? (yes/no): "):         
           contacts[edit]["phone"] = new_phone               
           print("Phone has successfully updated.")

        elif choice == "3":

            print(f"Current email: {contacts[edit]['email']}")   
            new_email = get_input("Enter a new email: ")          
            if new_email is None:                                 
              continue
            if yes_or_no("Save this change? (yes/no): "):         
              contacts[edit]["email"] = new_email               
              print("email has successfully updated.")

        elif choice == "4":
         
         print(f"Current city: {contacts[edit]['city']}")   
         new_city = get_input("Enter a new city: ")          
         if new_city is None:                                 
          continue
         if yes_or_no("Save this change? (yes/no): "):         
          contacts[edit]["city"] = new_city               
         print("city has successfully updated.")

        elif choice == "5":

            print(f"Current category: {contacts[edit]['category']}")   
            new_category = get_input("Enter a new category: ")          
            if new_category is None:                                 
             continue
            if yes_or_no("Save this change? (yes/no): "):         
             contacts[edit]["category"] = new_category               
            print("category has successfully updated.")
        else:
            print("invalid option try again")
def search_contacts():
 while True:
    search = get_input("Enter a name for searching: ")
    if search is None:
       return
    
    matched_contacts = {}


    for name , info in contacts.items():
       if search in name:
          matched_contacts[name] = info

    if not matched_contacts:
           print("contact was not found try again")

    else:
       print(f"there are {len(matched_contacts)} results with that name:")
       for number, (name, info) in enumerate(matched_contacts.items(), start=1):
        display_contacts(number,name,info)
          
menu()
