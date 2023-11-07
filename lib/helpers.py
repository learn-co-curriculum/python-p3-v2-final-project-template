# lib/helpers.py

from models.players import Player

"""VARIABLES"""
player_name = "Toaster"
char_name = "Gary the Goblin"

"""Main Menu Helpers"""

def view_all_players():
    print('-----------------------')
    print("Viewing all players...")
    for index, player in enumerate(Player.all()):
        print(f'{index + 1}. {player}')
    print('-----------------------')

# def view_profile_menu():
#     name = input('Name: ')
#     if name in [player.name for player in Player.all()]:
#         password = input('Password: ')
#         if password == Player.find_by_name(name)[0].name:

#     print("Enter your password:")

def view_players_in_next_session():
    print('-----------------------')
    print("Viewing players in next session...")
    for index, player in enumerate(Player.next_players()):
        print(f'{index + 1}. {player}')
    print('-----------------------')


def exit_program():
    print("Goodbye!")
    exit()


"""Profile Menu Helpers"""

def create_new_character():
    print("Creating new character...")

def view_all_characters():
    print("Viewing all characters...")

def view_active_characters():
    print("Viewing Active Characters...")

def delete_player():
    print(f"Deleting {player_name}'s profile")

def delete_character():
    print(f"Deleting {char_name}")

def rsvp():
    print("See you next session!")