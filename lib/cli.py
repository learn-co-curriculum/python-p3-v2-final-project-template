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
            create_sub()

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

def create_sub():
    while True:
        create_sub_menu()
        # need to incorporate input validation
        new_name = input("> ")

        if new_name == "back":
            break
        else:
            new_bio = input("Enter the new god's bio: ")
            if new_bio == "back":
                break
            else:
                parent = input("Enter the new god's parent (enter 'none' if new god has no parent): ")
                if parent == "back":
                    break
                else:
                    if parent == "none":
                        Parent.create(new_name, new_bio)
                        print(f"God {new_name} created successfully.")
                    else:
                        if parent in Parent.parent_names:
                            for a in Parent.all_parents:
                                parent_name = ""
                                if a.name == parent:
                                    parent_name = a
                                    Child.create(new_name, new_bio, parent_name)
                                    print(f"God {new_name} created successfully.")
                        else:
                            print(f"Parent {parent} not found. Please enter a valid parent name.")

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

def create_sub_menu():
    print('[Options]')
    print('type back to go back')
    print('type a new God\'s name to create them')

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