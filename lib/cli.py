# lib/cli.py
from models.players import Player

""" MAIN MENU CLI """
from helpers import (
    exit_program,
    view_all_players,
    view_players_in_next_session,  
)

from create_player import (
    create_new_player
)

def display_main_menu():
    while True:
        main_menu()
        choice = input("❯❯ ")
        if choice == "dm":
            print("It's a secret to everybody")
            password = input("❯❯ ")
            if password == "secret":
                run_dm_mode()
        elif choice == "0":
            exit_program()
        elif choice == "1":
            create_new_player()
        elif choice == "3":
            view_all_players()
        elif choice == "2":
            display_profile_menu()
        elif choice == "4":
            view_players_in_next_session()
        # elif choice == "5":
            # delete_player()
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    print("D&D Character Creator:")
    print("0. Exit the program")
    print("1. Create new player")
    print("2. View your profile")
    print("3. View all players")
    print("4. View players attending next session")
    # print("5. Delete a player")


""" PLAYER PROFILE CLI """
from helpers import (
    view_all_characters,
    get_active_char,
    delete_character,
    rsvp,
    delete_player,
    change_level,
    edit_active,
    cancel_game
)
from create_char import (
    create_new_char_menu
)

def display_profile_menu():
    current_player = None

    def profile_menu():
        print(f"★ {current_player.name}'s Profile ★") 
        print('-----------------------')
        print("0. Back to Main Menu")
        print("1. Create new character")
        print("2. View all characters")
        print("3. View your current character")
        print("4. RSVP for next session")
        print("5. Delete a character")
        print("6. Delete your profile")
        print('-----------------------')

    name = input('Name: ')
    name_list = [player.name.lower().strip() for player in Player.all()]
    if name.lower().strip() in name_list:
        index = name_list.index(name.lower().strip())
        password = input('Password: ')
        if password == [player for player in Player.all()][index].password:
            current_player = [player for player in Player.all()][index]
        else:
            print("Incorrect Password!")
    else:
        print("No user found with that name!")
        

    if current_player:
        while current_player:
            profile_menu()
            choice = input('❯❯ ')
            if choice == '0':
                break
            elif choice == '1':
                create_new_char_menu(current_player)
            elif choice == '2':
                print('-----------------------')
                print("Your Characters:")
                view_all_characters(current_player)
            elif choice == '3':
                print('-----------------------')
                print("Your Current Character:")
                get_active_char(current_player)
            elif choice == '4':
                rsvp(current_player)
            elif choice == '5':
                delete_character(current_player)
            elif choice == '6':
                deleted = delete_player(current_player)
                if deleted == True:
                    break
            else:
                print("Invalid choice. Please try again.")

def run_dm_mode():
    def dm_menu():
        print("★ Secret Dungeon Master Mode ★") 
        print('-----------------------')
        print("0. Back to Main Menu")
        print("1. See all characters")
        print("2. Change a characters level")
        print("3. Remove players from next game")
        print("4. Cancel next game")
        print('-----------------------')

    while True:
        dm_menu()
        choice = input('❯❯ ')
        if choice == '0':
            break
        elif choice == '1':
            view_all_characters('dm')
        elif choice == '2':
            change_level()
        elif choice == '3':
            edit_active()
        elif choice == '4':
            cancel_game()
        else:
            print('Invalid choice. Please try again.')

if __name__ == "__main__":
    display_main_menu()

