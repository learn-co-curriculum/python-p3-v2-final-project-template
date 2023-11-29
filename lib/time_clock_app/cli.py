from database import Session, initialize_db
from helpers import (
    exit_program,
    register_user,
    user_info,
    clock_in_user,
    clock_out_user
)

def main():
    session = Session()
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            register_user(session)
        elif choice == "2":
            clock_in_user(session)
        elif choice == "3":
            clock_out_user(session)
        elif choice == "4":
            user_info(session)
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Register new user")
    print("2. Clock in")
    print("3. Clock out")
    print("4. View user information")

if __name__ == "__main__":
    initialize_db()
    main()
