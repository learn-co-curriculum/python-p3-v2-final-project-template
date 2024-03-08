# lib/cli.py
import sqlite3
import ipdb
from models.member import Member
from models.locale import Locale

conn = sqlite3.connect('arcade.db')
cursor = conn.cursor()

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
        elif choice == "2":
            Locale.get_all()
        elif choice == "1":
            print("Inside view_all_members() func")
            Member.get_all()
        elif choice == "3":
            create_member()
        elif choice == "4":
            delete_member()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option")
    print("0. Exit the program")
    print("1. View all members")
    print("2. View all locations")
    print("3. Create new member")
    print("4. Delete a member")
    #build a create and a delete, update if possible

def exit_all():
    conn.close()
    print("Exiting the application")
    exit()

def view_all_members():
    # print("Inside view_all_members() function")
    cursor.execute("SELECT name FROM members")
    results = cursor.fetchall()
    # print("Printing results")
    print(results) 

    print("All Arcade members")
    for row in results:
        print(row[0])

def create_member():
    name_input = input("Enter name: ")
    tag_input = input("Enter tag: ")
    location_input = input("Enter location: ")
    var1 = Locale.find_by_location(location_input)

    member = Member(name_input, tag_input, location_input)
    member.save()

    print("New member has been aded!")

def delete_member():
    name = input("Enter member name to be deleted: ")
    Member.delete_by_name(name)
    print("Member deleted successfully.")

if __name__ == "__main__":
    main()
