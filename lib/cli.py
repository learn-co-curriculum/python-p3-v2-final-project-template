# lib/cli.py

from helpers import (
    exit_program,
    create_trip,
    list_trips,
    find_trip_by_id,
    find_trip_by_name,
    update_trip,
    delete_trip,
    create_activity,
    list_activities,
    find_activity_by_name,
    find_activity_by_id
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_trip()
        elif choice == "2":
            list_trips()
        elif choice == "3":
            delete_trip()
        elif choice == "4":
            update_trip()
        elif choice == "5":
            find_trip_by_id()
        elif choice == "6":
            find_trip_by_name()
        elif choice == "7":
            create_activity()
        elif choice == "8":
            list_activities()
        elif choice == "9":
            find_activity_by_name()
        elif choice == "10":
            find_activity_by_id()
        else:
            print("\033[31mInvalid choice\033[0m")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create new trip")
    print("2. List trips")
    print("3. Delete a trip")
    print("4. Update a trip")
    print("5. Find trip by id")
    print("6. Find trip by name")
    print("7. Create new activity")
    print("8. List activities")
    print("9. Find activity by id")
    print("10. Find activity by name")


if __name__ == "__main__":
    main()
