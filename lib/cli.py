# lib/cli.py
import sqlite3
from models.member import Member

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
        elif choice == "1":
            print("Inside view_all_members() func")
            view_all_members()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option")
    print("0. Exit the program")
    print("1. View all members")


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

if __name__ == "__main__":
    main()
