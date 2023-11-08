# lib/cli.py

from models.contact import Contact
from models.address import Address

def create_a_person():
    name = input("type name to create:")
    Contact.create(name)

def create_an_address():
    show_all_contacts()
    email = input(f"type email address: ")
    id = input(f"type id: ")
    Address.create(email, int(id))

def show_all_contacts():
    contacts = Contact.read_all()
    print("===all contacts===")
    for c in contacts:
        print(c)
    print("==============")
    return contacts

def show_all_addresses():
    addresses = Address.read_all()
    print("===all addresses===")
    for c in addresses:
        print(c)
    print("==============")
    return addresses

def find_by_id():
    try:
        id = int(input("Enter the contact ID: "))
        contact = Contact.get_id(id)
        if contact:
            print(f"Contact found: \n{contact}")
        else:
            print("Contact not found.")
    except ValueError:
        print("Invalid input. Please enter a valid contact ID.")

def exit_program():
    print("Goodbye!")
    exit()
    
def delete_contact():
    show_all_contacts()
    id = input("type the id to delete: ")
    Contact.delete(int(id))

def show_contact_detail():
    show_all_contacts()
    id = input("type the id to see the detail: ")
    Contact.show_detail(int(id))

def main():
    while True:
        menu()
        choice = input("> ")
        c = int(choice)
        if c == 0:
            exit_program()
        elif c == 1:
            create_a_person()
        elif c == 2:
            create_an_address()
        elif c == 3:
            show_all_contacts()
        elif c == 4:
            show_all_addresses()
        elif c == 5:
            delete_contact()
        elif c == 6:
            show_contact_detail()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. create a person")
    print("2. create an email address")
    print("3. show all contact")
    print("4. show all address")
    print("5. delete a contact")
    print("6. show a contact details")



if __name__ == "__main__": 
    main()
