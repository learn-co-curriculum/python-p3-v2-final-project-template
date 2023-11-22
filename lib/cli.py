# lib/cli.py
from models.world import World
from models.player import Player
from helpers import exit_program,clear_push,smol_push

selected_world = None
selected_player = None
def main():
    while True:
        menu()
        choice = input(">")
        clear_push()
        if choice == "1":
            clear_push()
            world_options()
        elif choice == "2":
            clear_push()
            player_options()
        elif choice == "3":
            clear_push()
            login_menu()
        elif choice == "4":
            clear_push()
            exit_program()
        else:
            clear_push()
            print("Please Make A Valid Choice")

def menu():
    clear_push()
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
            clear_push()
            create_world_menu()
        elif choice == "2":
            if World.all() == []:
                clear_push()
                print("")
                print("There Are No Worlds\n Please Create One")
            else:
                clear_push()
                print(World.all())
                select_world()
        elif choice == "3":
            while True:
                print("___________")
                print(World.all())
                print("-----------")
                print("Select World Id to Delete")
                print("Press 0 to return")
                ids = input("->")
                if ids == "0":
                    break
                elif ids == "":
                    clear_push()
                    print("? You gonna smash some worlds?, if not you can leave with 0")
                elif int(ids) > len(World.all()):
                    clear_push()
                    print("we destory worlds here not made up stuff, leave with 0")
                else:
                    world = World.find_by_id(ids)
                    world.shatter()
                    clear_push()
                    print("World Destroyed")
                    print("Odd thing for a player Aint it?")
        elif choice == "4":
            break
        else:
            print("Please Make A Valid Choice")
        
def login_menu():
    while True:
        clear_push()
        print(f"World Selected:{selected_world}")
        if selected_world == None:
            print("")
            print("Perhaps you should go select a player?")
        print("")
        print(f"Player Selected:{selected_player}")
        if selected_world == None:
            print("")
            print("Perhaps you should go select a player?")
        print("")
        print("you can go back with 0")
        
        if selected_world and selected_player != None:
            print("press 1 to login with the selection")
        choice = input(">")
        if choice == "0":
            break
        elif choice == "1":
            if selected_world and selected_player != None:
                selected_player.login(selected_world)
                login_que()
            else:
                print("Hmm? you can't join without a selection.")
def world_menu():
    clear_push()
    print("________________________")
    print("World Menu")
    print("------------------------")
    print("1. Create World")
    print("2. Display Worlds")
    print("3. Delete World")
    print("4. Back to Main Menu")

def login_que():
    while True:
        smol_push()
        print("Logged in successfully please wait \n ...")
        print("Que Position is: 9,023,123,333,404")
        choice = input("Thinking Of Leaving? type: 'im not waiting' to exit que>")
        if choice == "no":
            clear_push()
            print("Suit Yourself.")
        elif choice == "im not waiting":
            break
        else:
            clear_push()
            print("Those are not the magic words.")

def player_options():
    while True:
        player_menu()
        choice = input(">")
        if choice == "1":
            clear_push()
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
            id = input('Please input a world id: ')
            print(f"World: {id}")
            name= input('Please input a player name: ')
            if id and name:
                player = Player.find_by_name(name)
                world_instance = World.find_by_id(id)
                if player and world_instance:
                    player.login(world_instance)
                    login_que()
                else:
                    print('Player or world not found')
            else: 
                print('Please enter a valid world id and player name')
        elif choice == '6':
            print(Player.all())
            name = input('please input player name ')
            if name:
                player = Player.find_by_name(name)
                if player:
                    print(player.worlds())   
                else:
                    print('Player not found')
            else:
                print(' please enter a valid name')
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
            clear_push()
            print("____________________")
            print("Please Name Yourself")
        elif len(choice) > 11:
            clear_push()
            print("___________________________")
            print("Please Enter A Shorter Name")
        else:
            clear_push()
            print("A New Challenger Approachs!")
            Player.create(choice)
            print("")
            print(f"And Their Name is: {choice}")
            print("")
            print("You Sure you want that name? Perhaps you should try from scratch again...")
            print("")
            # selected_player = Player.find_by_id(choice) -- cant seem to get this to work when create()
def create_world_menu():
    while True:
        print("____________________")
        print("Press 0 to go back")
        choice = input("What Is Your World Called Traveler? >")
        if choice == "0":
            break
        elif choice == "":
            clear_push()
            print("________________________________________")
            print("No Input Detected: Please Name The World")
        elif len(choice) > 16:
            clear_push()
            print("___________________________")
            print("Please Enter A Shorter Name....")
        else:
            print(World.create(choice))
            clear_push()
            print("Very Creative with your names are you?")
            print(f"Created: {choice}")
            print(f"By all means make another")

def player_menu():
    clear_push()
    print("________________________")
    print("Player Menu")
    print("------------------------")
    print('''1.                                                     
  / __|| |_   ___  ___  ___ ___   _  _  ___  _  _  _ _   / __|| |_   __ _  _ _  __ _  __ | |_  ___  _ _ 
 | (__ | ' \ / _ \/ _ \(_-</ -_) | || |/ _ \| || || '_| | (__ | ' \ / _` || '_|/ _` |/ _||  _|/ -_)| '_|
  \___||_||_|\___/\___//__/\___|  \_, |\___/ \_,_||_|    \___||_||_|\__,_||_|  \__,_|\__| \__|\___||_|''')

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
