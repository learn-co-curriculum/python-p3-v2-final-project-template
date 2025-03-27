# lib/cli.py

from helpers import (
    exit_program,
    create_course,
    display_courses,
    update_course,
    delete_course,
    find_by_coursename
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_course()
        elif choice == "2":
            display_courses()
        elif choice == "3":
            update_course()
        elif choice == "4":
            delete_course()
        elif choice == "5":
            find_by_coursename()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create Course")
    print("2. Display Course")
    print("3. Update Course")
    print("4. Delete Course")
    print("5. Find Course by coursename")


if __name__ == "__main__":
    main()
