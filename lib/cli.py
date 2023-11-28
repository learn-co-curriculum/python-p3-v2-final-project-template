# lib/cli.py

from helpers import (
    exit_program,
    create_username,
    create_password
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_username()
        elif choice == "2":
            create_password()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. create username")
    print("2. create password")


if __name__ == "__main__":
    main()
