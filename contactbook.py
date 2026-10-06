contacts = {
    "Ram": "9841000000",
    "Sita": "9851000000",
    "Hari": "9861000000"
}

while True:
    print("1. Add a new contact")
    print("2. Search for a contact")
    print("3. Update an existing contact")
    print("4. Delete a contact")
    print("5. Display all contacts")
    print("6. Exit the program")

    n = int(input("Enter your choice: "))

    if n == 1:
        name = input("Enter name: ").capitalize()
        contact = input("Enter contact: ")

        if len(contact) == 10:
            contacts[name] = contact
            print("Contact Added Successfully.")
        else:
            print("Number must be 10 digits.")

    elif n == 2:
        name = input("Enter Name: ").capitalize()

        if name in contacts:
            print("Contact:", contacts[name])
        else:
            print("Person Not Found.")

    elif n == 3:
        name = input("Enter name of contact to update: ").capitalize()

        if name in contacts:
            choice = int(input("Change 1. Name or 2. Number: "))

            if choice == 1:
                username = input("Enter new name: ").capitalize()
                contacts[username] = contacts.pop(name)
                print("Name Updated.")

            elif choice == 2:
                usercontact = input("Enter new number: ")

                if len(usercontact) == 10:
                    contacts[name] = usercontact
                    print("Contact Updated.")
                else:
                    print("Number must be 10 digits.")

            else:
                print("Invalid Choice.")

        else:
            print("Person Not Found.")

    elif n == 4:
        name = input("Enter name of contact to delete: ").capitalize()

        if name in contacts:
            contacts.pop(name)
            print("Contact Deleted Successfully.")
        else:
            print("No Contact Found.")

    elif n == 5:
        print(contacts)

    elif n == 6:
        print("Exited")
        break

    else:
        print("Invalid Choice.")