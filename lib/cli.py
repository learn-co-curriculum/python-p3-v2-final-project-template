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
            login_menu()
            # Would be a menu()
                # while True:
                    # login_menu()
                    # Choice == "1":
                    #     select_player()
                    # choice == "2":
                    #     select_world()
        elif choice == "4":
            exit_program()
        else:
            print("Please Make A Valid Choice")

def menu():
    print("""
            .,-:;//;:=,
         . :H@@@MM@M#H/.,+%;,
      ,/X+ +M@@M@MM%=,-%HMMM@X/,
     -+@MM; $M@@MH+-,;XMMMM@MMMM@+-
    ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.
  ,%MM@@MH ,@%=            .---=-=:=,.
  -@#@@@MX .,              -%HX$$%%%+;
 =-./@M@M$                  .;@MMMM@MM:
 X@/ -$MM/                    .+MM@@@M$
,@M@H: :@:                    . -X#@@@@-
,@@@MMX, .                    /H- ;@M@M=
.H@@@@M@+,                    %MM+..%#$.
 /MMMM@MMH/.                  XM@MH; -;
  /%+%$XHH@$=              , .H@@@@MX,
   .=--------.           -%H.,@@@@@MX,
   .%MM@@@HHHXX$$$%+- .:$MMX -M@@MM%.
     =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=
       =%@M@M#@$-.=$@MM@@@M; %M%=
         ,:+$+-,/H#MMMMMMM@- -,
               =++%%%%+/:-.
""")
    print("________________________")
    print("Please select an option")
    print("------------------------")
    print("1. World Options")
    print("2. Player Options")
    print("3. Login Screen?")
    print("4. Exit the program")

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
    print("Theres Nothing Here Right Now")
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
        elif choice == '5':
            id = input('Please input a id')
            name= input('Please input a name')
            player = Player.find_by_name(name)
            world_instance = World.find_by_id(id)
            player.login(world_instance)
            player.worlds()
        elif choice == '6':
            name = input('please input player name ')
            player = Player.find_by_name(name)
            print(player.worlds())   
        elif choice == "7":
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
    print("5. Login A player to a world")
    print("6. Search a Player Worlds")
    print("7. Back to Main Menu")

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
