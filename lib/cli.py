# lib/cli.py
from models.Parent import Parent,Child

def reset_database():
    Parent.drop_table()
    Parent.create_table()
    Child.drop_table()
    Child.create_table()
reset_database()
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
            print(f'{Parent.get_all_parents()+Child.get_all_children()}')
        
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
        print(f'{Parent.get_all_parents()+Child.get_all_children()}')
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
            Parent.parent_names.remove(sub_choice)
            for a in Parent.all_parents:
                if a.name == sub_choice:
                    a.delete()
                    Parent.all_parents.remove(a)
                    print(f'{a.name} has been deleted')
        elif sub_choice in Child.name_list:
            Child.name_list.remove(sub_choice)
            for a in Child.spawn:
                if a.name == sub_choice:
                    a.delete()
                    Child.spawn.remove(a)
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
