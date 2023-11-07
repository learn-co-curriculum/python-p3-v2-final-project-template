# lib/cli.py

from models.contact import Contact
from models.address import Address

def create_a_person():
    name = input("type name to create:")
    person = Contact(name)
    person.create()

def create_an_address():
    if Contact.latest != None and len(Contact.latest.name):
        email = input(f"type email address for {Contact.latest}")
        address = Address(email, Contact.latest.id)
        address.create()
    else:
        print("should read or create a person first")

def show_all_contacts():
    contacts = Contact.read_all()
    print("===all contacts===")
    for c in contacts:
        print(c)
    print("==============")

def show_all_addresses():
    addresses = Address.read_all()
    print("===all addresses===")
    for c in addresses:
        print(c)
    print("==============")

def exit_program():
    print("Goodbye!")
    exit()


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
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. create a person")
    print("2. create an email address")
    print("3. show all contact")
    print("4. show all address")


if __name__ == "__main__":
    main()
