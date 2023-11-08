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
    print("________________________")
    print("Please select an option")
    print("------------------------")
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
            if World.all() == []:
                print("")
                print("There Are No Worlds\n Please Create One")
            else:
                print(World.all())
                select_world()
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
    print("________________________")
    print("World Menu")
    print("------------------------")
    print("1. Create World")
    print("2. Display Worlds")
    print("3. Delete World")
    print("4. Back to Main Menu")

def player_options():
    while True:
        player_menu()
        choice = input(">")
        if choice == "1":
            create_player_menu()
        elif choice == "2":
            if Player.all() == []:
                print("")
                print("There Are No Players\n Please Create One")
            else:
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


def create_player_menu():
    while True:
        print("Press 0 to go back")
        choice = input("What Is Your Name Traveler?:>")
        if choice == "0":
            break
        elif choice == "":
            print("Please Name Yourself")
        else:
            print(Player.create(choice))
            break

def player_menu():
    print("________________________")
    print("Player Menu")
    print("------------------------")
    print("1. Create Player")
    print("2. Display Player's")
    print("3. Remove Player")
    print('4. Find Player by name')
    print("5. Back to Main Menu")

def select_world():
    while True:
        selection = input("Select a world id or backout with 0: >")
        if selection == "0":
            break
        elif selection == "":
            print("Please Select a world ID or backout with 0: ")
        elif int(selection) <= len(World.all()):
            print(f'Selected\n{World.find_by_id(selection)}')
        else:
            print("Please Select a valid world ID")
if __name__ == "__main__":
    main()
