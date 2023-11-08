# lib/cli.py
from models.world import World
from models.player import Player
from helpers import exit_program


def main():
    while True:
        menu()
        choice = input(">")
        if choice == "1":
            world_options()
        elif choice == "2":
            player_options()
        elif choice == "3":
            exit_program()
        else:
            print("Please Make A Valid Choice")

def menu():
    print("Please select an option:")
    print("1. World Options")
    print("2. Player Options")
    print("3. Exit the program")

def world_options():
    while True:
        world_menu()
        choice = input(">")
        if choice == "1":
            print("What Is Your World Called Traveler?")
            World.create(input("->"))
        elif choice == "2":
            print(World.all())
        elif choice == "3":
            print("Select World Id to Delete")
            id = input("->")
            world = World.find_by_id(id)
            world.shatter()
        elif choice == "4":
            break
        else:
            print("Please Make A Valid Choice")

def world_menu():
    print("World Menu:")
    print("1. Create World")
    print("2. Display Worlds")
    print("3. Delete World")
    print("4. Back to Main Menu")

def player_options():
    while True:
        player_menu()
        choice = input(">")
        if choice == "1":
            print("What Is Your Name Traveler?")
            Player.create(input("->"))
        elif choice == "2":
            print(Player.all())
        elif choice == "3":
            id = input("Select Player Id to Delete:")
            player = Player.find_by_id(id)
            player.deletes()
        elif choice == '4':
            name = input('Find your character by their name: ')
            player = Player.find_by_name(name)
            print(player)
        elif choice == "5":
            break
        else:
            print("Please Make A Valid Choice")

def player_menu():
    print("Player Menu")
    print("1. Create Player")
    print("2. Display Player's")
    print("3. Remove Player")
    print('4. Find Player by name')
    print("5. Back to Main Menu")

if __name__ == "__main__":
    main()
