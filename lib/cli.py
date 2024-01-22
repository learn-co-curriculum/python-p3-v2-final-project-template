# lib/cli.py

from helpers import (
    exit_program,
    create_new_player,
    list_all_players,
    update_player,
    delete_player,
    list_all_levels
)
from models.player import Player
from models.pet import Pet

def main():
    while True:
        print("---Python Type-On---")
        print("Welcome to Python Type-On!")
        
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_new_player()
        elif choice == "2":
            list_all_players()
        elif choice == "3":
            update_player()
        elif choice == "4":
            delete_player()
        elif choice == "5":
            list_all_levels()
        elif choice == "6":
            pass
        elif choice == "7":
            pass
        elif choice == "8":
            pass
        else:
            print("Invalid choice")


def menu():
    
    print("0. Exit the program")
    print("1. New game")
    print("2. List all players")
    print("3. Update player")
    print("4. Delete player")
    print("5. List all levels")

if __name__ == "__main__":
    main()
