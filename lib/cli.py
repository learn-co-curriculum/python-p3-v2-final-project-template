# lib/cli.py
from models.Parent import Parent,Child

Zeus=Parent('Zeus','this is a bio')
Metis=Parent('Metis','Metis bio')
Athena=Child('Athena','Athena bio',Zeus)

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
            Parent.names()
        elif choice in Parent.parent_names:
            for a in Parent.all_parents:
                bio=''
                if a.name == choice:
                    bio=a.bio
                    print(bio)
        elif choice in Child.name_list:
            for a in Child.spawn:
                bio=''
                if a.name == choice:
                    bio=a.bio
                    print(bio)
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
