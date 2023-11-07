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
        choice = input("> ")
        if choice == "0":
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
    player_name,
    view_all_characters,
    view_active_characters,
    delete_player,
    delete_character,
    rsvp
)
from create_char import (
    create_new_char_menu
)

def display_profile_menu():
    current_player = None

    def profile_menu():
        """profile title should include player.name"""
        print(f"{current_player.name}'s Profile:") 
        print("0. Back to Main Menu")
        print("1. Create new character")
        print("2. View all characters")
        print("3. View your active characters")
        print("4. RSVP for next session")
        print("5. Delete a character")
        print("6. Delete your profile")

    name = input('Name: ')
    password = input('Password: ')
    if (name in [player.name for player in Player.all()] and 
        password == Player.find_by_name(name)[0].password):
        current_player = Player.find_by_name(name)[0]
    else:
        print("Incorrect Login.")
    
    if current_player:
        while True:
            profile_menu()
            choice = input('** ')
            if choice == '0':
                break
            elif choice == '1':
                create_new_char_menu()
            elif choice == '2':
                view_all_characters()
            elif choice == '3':
                view_active_characters()
            elif choice == '4':
                rsvp()
            elif choice == '5':
                delete_character()
            elif choice == '6':
                delete_player()    
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    display_main_menu()


# import helpers
# 
# profile_choice = input("> ")
# 
# if profile_choice == '0':
#   break
# elif profile_choice in ['1', '2', '3']:
#   profile_actions ={
#       '1': helpers.create_character,
#       '2': helpers.view_characters
# } 
#   profile_actions[profile_choice]()
# 
# 
# 
# 
