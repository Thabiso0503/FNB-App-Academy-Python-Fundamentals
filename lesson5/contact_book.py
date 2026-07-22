# List to store all contacts
contacts = []

# Function to add a contact
def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("Contact added successfully!\n")


# Function to search for a contact
def search_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None


# Function to delete a contact
def delete_contact(name):
    contact = search_contact(name)

    if contact:
        contacts.remove(contact)
        print("Contact deleted successfully!\n")
    else:
        print("Contact not found.\n")


# Function to display all contacts
def view_all():
    if len(contacts) == 0:
        print("No contacts available.\n")
    else:
        print("\n----- Contact List -----")
        for contact in contacts:
            print(f"Name : {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print("-" * 25)
        print()


# Main menu
while True:
    print("====== Contact Book ======")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        name = input("Enter the name to search: ")
        result = search_contact(name)

        if result:
            print("\nContact Found")
            print(f"Name : {result['name']}")
            print(f"Phone: {result['phone']}")
            print(f"Email: {result['email']}\n")
        else:
            print("Contact not found.\n")

    elif choice == "3":
        name = input("Enter the name to delete: ")
        delete_contact(name)

    elif choice == "4":
        view_all()

    elif choice == "5":
        print("Thank you for using Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a number between 1 and 5.\n")
