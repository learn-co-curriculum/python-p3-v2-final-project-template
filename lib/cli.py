import sqlite3
from models.member import Member
from models.locale import Locale
from helpers import exit_program

conn = sqlite3.connect('arcade.db')
cursor = conn.cursor()

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            print("Inside view_all_members() func")
            view_all_members()
        elif choice == "2":
            view_all_locations()
        elif choice == "3":
            create_member()
        elif choice == "4":
            Member.delete_member()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option")
    print("0. Exit the program")
    print("1. View all members")
    print("2. View all locations")
    print("3. Create new member")
    print("4. Delete a member")

def view_all_members():
    cursor.execute("SELECT name FROM members")
    results = cursor.fetchall()
    print("All Arcade members:")
    for row in results:
        print(row[0])

def view_all_locations():
    locations = Locale.get_all()
    print("All Locations:")
    for location in locations:
        print(location)

def create_member():
    name_input = input("Enter name: ")
    tag_input = input("Enter tag: ")
    location_input = input("Enter location: ")
    locale_id = Locale.get_id_by_location(location_input) 
    member.save()
    # this will fetch the location input
    # member = Member(name_input, tag_input, location_input) parker

if __name__ == "__main__":
    main()