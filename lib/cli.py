# lib/cli.py
from models.world import World
from models.player import Player
from helpers import exit_program

selected_world = None
selected_player = None
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
        elif choice == "4":
            login_menu()
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
        print(selected_world)
        choice = input(">")
        if choice == "1":
            create_world_menu()
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
        
def login_menu():
    print(f"World Selected:{selected_world}")
    print(f"Player Selected:{selected_player}")

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
                select_player()
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
            print("____________________")
            print("Please Name Yourself")
        elif len(choice) > 11:
            print("___________________________")
            print("Please Enter A Shorter Name")
        else:
            print(Player.create(choice))
            break
def create_world_menu():
    while True:
        print("____________________")
        print("Press 0 to go back")
        choice = input("What Is Your World Called Traveler? >")
        if choice == "0":
            break
        elif choice == "":
            print("________________________________________")
            print("No Input Detected: Please Name The World")
        elif len(choice) > 16:
            print("___________________________")
            print("Please Enter A Shorter Name")
        else:
            print(World.create(choice))
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
            print("Please Select a world ID or backout with 0: >")
        elif int(selection) <= len(World.all()):
            global selected_world
            selected_world = World.find_by_id(selection)
            print(f'Selected\n{selected_world}')
        else:
            print("Please Select a valid world ID")
def select_player():
    while True:
        selection = input("Select a player id or backout with 0: >")
        if selection == "0":
            break
        elif selection == "":
            print("Please Select a Player with ID or backout with 0")
        elif int(selection) <= len(Player.all()):
            global selected_player
            selected_player = Player.find_by_id(selection)
            print(f'Selected\n{selected_player}')
        else:
            print("Please Select a valid Player ID")
if __name__ == "__main__":
    main()
