# lib/cli.py
from models.Parent import Parent,Child

Parent.drop_table()
Parent.create_table()
Child.drop_table()
Child.create_table()

Poseidon=Parent.create('Poseidon','this is a bio')
Demeter=Parent.create('Demeter','Demeter bio')
Theseus=Child.create('Theseus','Theseus bio',Poseidon)

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
            list_sub()
        
        elif choice == "3":
            pass

        elif choice == "4":
            delete_sub()

        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")
    print("2. A list of the Gods")
    print("3. Add a God")
    print("4. Delete a god")

def list_sub():
    while True:
        list_sub_menu()
        Parent.names()
        sub_choice = input("> ")
        if sub_choice in Parent.parent_names:
            for a in Parent.all_parents:
                bio=''
                if a.name == sub_choice:
                    print('[BIO]')
                    print(a.bio)
        elif sub_choice in Child.name_list:
            for a in Child.spawn:
                bio=''
                if a.name == sub_choice:
                    print('[BIO]')
                    print(a.bio)
        elif sub_choice == "back":
            break
        else:
            print('[invalid choice, try again.]')

def delete_sub():
    while True:
        delete_sub_menu()
        sub_choice=input("> ")
        if sub_choice in Parent.parent_names:
            for a in Parent.all_parents:
                if a.name == sub_choice:
                    a.delete()
                    print(f'{a.name} has been deleted')
        elif sub_choice in Child.name_list:
            for a in Child.spawn:
                if a.name == sub_choice:
                    a.delete()
                    print(f'{a.name} has been deleted')
        elif sub_choice == "back":
            break
        else:
            print('invalid')

def delete_sub_menu():
    print('[Options]')
    print('type back to go back')
    print('type a God\'s name to delete them')

def list_sub_menu():
    print('[Options]')
    print('Type back to go back')
    print('(Type a God\'s name from the names below)')


if __name__ == "__main__":
    main()
