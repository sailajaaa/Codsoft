import json

def add_contact():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone_number": phone_number,
        "email": email,
        "address": address
    }

    with open("contacts.json", "r+") as file:
        data = json.load(file)
        data.append(contact)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()

    print("Contact added successfully!")

def view_contacts():
    with open("contacts.json", "r") as file:
        data = json.load(file)

        if not data:
            print("No contacts found.")
        else:
            print("Contact List:")
            for i, contact in enumerate(data, 1):
                print(f"{i}. Name: {contact['name']}, Phone: {contact['phone_number']}, Email: {contact['email']}, Address: {contact['address']}")

def search_contact():
    search_query = input("Enter name or phone number to search: ")

    with open("contacts.json", "r") as file:
        data = json.load(file)

        found_contacts = [contact for contact in data if search_query.lower() in contact['name'].lower() or search_query in contact['phone_number']]

        if found_contacts:
            print("Search Results:")
            for i, contact in enumerate(found_contacts, 1):
                print(f"{i}. Name: {contact['name']}, Phone: {contact['phone_number']}, Email: {contact['email']}, Address: {contact['address']}")
        else:
            print("No contacts found.")

def update_contact():
    search_query = input("Enter name or phone number to search: ")

    with open("contacts.json", "r+") as file:
        data = json.load(file)

        found_contacts = [contact for contact in data if search_query.lower() in contact['name'].lower() or search_query in contact['phone_number']]

        if found_contacts:
            print("Select a contact to update:")
            for i, contact in enumerate(found_contacts, 1):
                print(f"{i}. Name: {contact['name']}, Phone: {contact['phone_number']}")

            choice = int(input("Enter your choice: ")) - 1
            selected_contact = found_contacts[choice]

            print("Enter new details:")
            new_name = input("New name: ")
            new_phone_number = input("New phone number: ")
            new_email = input("New email: ")
            new_address = input("New address: ")

            selected_contact['name'] = new_name
            selected_contact['phone_number'] = new_phone_number
            selected_contact['email'] = new_email
            selected_contact['address'] = new_address

            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()

            print("Contact updated successfully!")
        else:
            print("No contacts found.")

def delete_contact():
    search_query = input("Enter name or phone number to search: ")

    with open("contacts.json", "r+") as file:
        data = json.load(file)

        found_contacts = [contact for contact in data if search_query.lower() in contact['name'].lower() or search_query in contact['phone_number']]

        if found_contacts:
            print("Select a contact to delete:")
            for i, contact in enumerate(found_contacts, 1):
                print(f"{i}. Name: {contact['name']}, Phone: {contact['phone_number']}")

            choice = int(input("Enter your choice: ")) - 1
            selected_contact = found_contacts[choice]

            data.remove(selected_contact)

            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()

            print("Contact deleted successfully!")
        else:
            print("No contacts found.")

def main():
    try:
        with open("contacts.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Contacts file not found. Creating a new one...")
        data = []
        with open("contacts.json", "w") as file:
            json.dump(data, file)

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1: 
            add_contact(data)
        elif choice == 2:
            view_contacts(data)
        elif choice == 3:
            search_contact(data)
        elif choice == 4:
            update_contact(data)
        elif choice == 5:
            delete_contact(data)
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

        with open("contacts.json", "w") as file:
            json.dump(data, file, indent=4)

if __name__ == "__main__":
    main()