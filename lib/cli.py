# lib/cli.py

from helpers import (
    exit_program,
    add_member,
    change_membership, 
    view_members,
    view_classes,
    add_class,
    delete_member, 
    delete_class,
    delete_trainer
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_member()
        elif choice == "2":
            change_membership()
        elif choice == "3":
            view_members()
        elif choice == "4":
            view_classes()
        elif choice == "5":
            add_class()
        elif choice == "6":
            delete_member()
        elif choice == "7":
            delete_class()
        elif choice == "8":
            delete_trainer()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add New Gym Member")
    print("2. Change Membership Plan")
    print("3. View Members")
    print("4. View Exercise Classes")
    print("5. Add New Exercise Class")
    print("6. Delete Members")
    print("7. Delete Exercise Classes")
    print("8. Delete Trainer")



if __name__ == "__main__":
    main()
