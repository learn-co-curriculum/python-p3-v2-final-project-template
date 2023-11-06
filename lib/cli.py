# lib/cli.py
from models.Parent import Parent
from models.Children import Child

p1=Parent('zeus','this is a bio')
c1=Child('Athena','Athena bio',p1)

from helpers import (
    exit_program,
    helper_1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            p1.my_children()
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
