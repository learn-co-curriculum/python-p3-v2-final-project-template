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
        
        elif choice == "2":
            sub()

        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")
    print("2. Bio")

def sub():
    while True:
        sub_menu()
        sub_choice = input("> ")
        if sub_choice in Parent.parent_names:
            for a in Parent.all_parents:
                bio=''
                if a.name == sub_choice:
                    bio=a.bio
                    print('[BIO]')
                    print(bio)
        elif sub_choice in Child.name_list:
            for a in Child.spawn:
                bio=''
                if a.name == sub_choice:
                    bio=a.bio
                    print('[BIO]')
                    print(bio)
        elif sub_choice == "back":
            break
        else:
            print('[invalid choice, try again.]')

def sub_menu():
    print('[Options]')
    print('Type back to go back')
    print('Type a God\'s name')


if __name__ == "__main__":
    main()
