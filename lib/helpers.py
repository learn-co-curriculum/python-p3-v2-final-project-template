# lib/helpers.py

"""VARIABLES"""
player_name = "Toaster"
char_name = "Gary the Goblin"

"""Main Menu Helpers"""

def create_new_player():
    print("Creating new player...")

def view_all_players():
    print("Viewing all players...")

def view_profile_menu():
    print("Enter your password:")

def view_players_in_next_session():
    print("Players attending next session")


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