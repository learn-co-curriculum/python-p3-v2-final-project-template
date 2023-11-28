# lib/cli.py

from helpers import (
    exit_program,
    create_username
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_username()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. create username")


if __name__ == "__main__":
    main()
