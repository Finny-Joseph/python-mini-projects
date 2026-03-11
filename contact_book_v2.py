contacts = {}

print("===== Contact Book =====")

def add_contact():
    name = input("Enter Contact name: ").strip()
    number = input("Enter Contact Number: ").strip()
    contacts[name] = number
    print("Contact Saved!")

def view_contacts():
    print("Saved Contacts:")
    for name, number in contacts.items():
        print(name, ":" , number)

def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print("Phone:",contacts[name])
    else:
        print("Contact not Found")

def delete_contact():
    name = input("Enter Contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact Deleted.")
    else:
        print("Contact Not Found.")

while True:
    options = input("1 Add Contact\n2 View Contacts\n3 Search Contact\n4 Delete Contact\n5 Exit\n Choose option: ")

    if options == "1":
        add_contact()
    elif options == "2":
        view_contacts()
    elif options == "3":
        search_contact()
    elif options == "4":
        delete_contact()
    elif options == "5":
        print("GoodBye!")
        break
    else:
        print("Invalid Choice")


