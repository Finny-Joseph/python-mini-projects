import json

def load_contacts():
    try:
        with open("contacts.json","r") as file:
            return json.load(file)
    except:
        return{}

contacts = load_contacts()

print("===== Contact Book =====")

def save_contacts():
    with open("contacts.json","w") as file:
        json.dump(contacts, file)

def add_contact():
    name = input("Enter Contact name: ").strip()
    number = input("Enter Contact Number: ").strip()
    if name in contacts:
        print("Contact already exists!")
        return
    contacts[name] = number
    save_contacts()
    print("Contact Saved!")

def view_contacts():
    if not contacts:
        print("No contacts saved.")
        return
    print("Saved Contacts:")
    for name, number in contacts.items():
        print(f"{name}: {number}")

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
        save_contacts()
        print("Contact Deleted.")
    else:
        print("Contact Not Found.")

def update_contact():
    name = input("Enter contact to update: ").strip()
    if name in contacts:
        new_number = input("Enter new number: ").strip()
        contacts[name] = new_number
        save_contacts()
        print("Contact Updated!")
    else:
        print("Contact Not Found.")

while True:
    options = input("1 Add Contact\n2 View Contacts\n3 Search Contact\n4 Delete Contact\n5 Update Contact\n6 Exit\n Choose option: ")

    if options == "1":
        add_contact()
    elif options == "2":
        view_contacts()
    elif options == "3":
        search_contact()
    elif options == "4":
        delete_contact()
    elif options == "5":
        update_contact()
    elif options == "6":
        print("GoodBye!")
        break
    else:
        print("Invalid Choice")


