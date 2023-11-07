# lib/cli.py
from models.world import World
from models.player import Player
from helpers import (
    exit_program,
)


def main():
    while True:
        menu()
        choice = input(">")
        if choice == "0":
            print("What Is Your World Called Traveler?")
            World.create(input("->"))
        elif choice == "1":
            print(World.all())
        elif choice == "2":
            print("Select World Id to Delete")
            id = input("->")
            world = World.find_by_id(id)
            world.shatter()
        elif choice == "3":
            print("What Is Your Name Traveler?")
            Player.create(input("->"))
        elif choice == "4":
            print(Player.all())
        elif choice == "5":
            print("Select Player Id to Delete")
            id = input("->")
            player = Player.find_by_id(id)
            player.deletes()
        elif choice == "6":
            exit_program()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Create World")
    print("1. Display World's")
    print("2. Delete World")
    print("3. Create Player")
    print("4. Display Player's")
    print("5. Remove Player")
    print("6. Exit the program")
if __name__ == "__main__":
    main()

# someint=World("Input")