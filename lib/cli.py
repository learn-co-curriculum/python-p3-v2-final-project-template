# lib/cli.py

from helpers import (
    exit_program,
    helper_1,
    create_trip,
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_trip()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create new trip")


if __name__ == "__main__":
    main()
