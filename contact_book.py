contacts = {}

while True:
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")

    contacts[name] = phone

    cont = input("Add one more contact? (y/n): ")

    if cont.lower() == "n":
        break

print("\nSaved Contacts:")

for name, phone in contacts.items():
    print(name, ":", phone)