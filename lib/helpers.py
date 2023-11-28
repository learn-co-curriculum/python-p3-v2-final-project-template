# lib/helpers.py
from time_clock_app.user_info import Username
import os 


def create_username():
    os.system('cls' if os.name == 'nt' else 'clear')
    user = input("enter unsername: ")
    username = Username(user)
    print (f'your username is: {username}')
    return username
    
def create_password():
    os.system('cls' if os.name == 'nt' else 'clear')
    password = input("enter password: ")
    print(f'your password is: {password}')

def user_info():
    os.system('cls' if os.name == 'nt' else 'clear')
    user_menu()

    choice = input("> ")
    if choice == "0":
        exit_program
    elif choice == "1":
        print("______password/username______")
        print("")
    elif choice == "2":
        print("  ______clock-in times______")
        print("place holder for clock-out times")
        print("")
    elif choice == "3":
        print("______clock-out times______")
        print("place holder for clock-out times")
        print("")
    else:
        print("______Invalid choice______")
        print("")

def user_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Please select an action:")
    print("0. exit")
    print("1. manage username/password")
    print("2. see clock-in time")
    print("3. see clock-out time")

def exit_program():
    print("Goodbye!")
    os.system('cls' if os.name == 'nt' else 'clear')
    
    exit()
