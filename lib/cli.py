# lib/cli.py
import sqlite3

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
            helper_1()
        elif choice == "2":
            view_all_members()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option")
    print("0. Exit the program")
    print("1.nada")
    print("2. View all members")

def exit_all():
    conn.close()
    print("Exiting the application")
    exit()

def view_all_members():
    cursor.execute("SELECT * FROM members")
    results = cursor.fetchall()

    print("All Arcade members")
    for row in results:
        print(row[1])

def helper_1():
    cursor.execute("SELECT * FROM arcades")
    results = cursor.fetchall()

    for row in results:
        print(row)

if __name__ == "__main__":
    main()
