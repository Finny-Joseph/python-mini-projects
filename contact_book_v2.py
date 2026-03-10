contacts = {}

print("===== Contact Book =====")

def add_contact():
    name = input("Enter Contact name: ")
    number = input("Enter Contact Number: ")
    contacts[name] = number
    print("Contact Saved!")

def view_contacts():
    print("Saved Contacts:")
    for name, number in contacts.items():
        print(name, ":" , number)

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print("Phone:",contacts[name])
    else:
        print("Contact not Found")

while True:
    options = input("1 Add Contact\n2 View Contacts\n3 Search Contact\n4 Exit\n Choose option: ")

    if options == "1":
        add_contact()
    elif options == "2":
        view_contacts()
    elif options == "3":
        search_contact()
    elif options =="4":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice")


