# lib/helpers.py

from models.players import Player
from models.characters import Character


"""Main Menu Helpers"""

def view_all_players():
    print('-----------------------')
    print("Viewing all players...")
    for index, player in enumerate(Player.all()):
        print(f'{index + 1}. {player}')
    print('-----------------------')

def view_players_in_next_session():
    print('-----------------------')
    print("RSVP'd Players")
    players = Player.view_next_players()
    for index, player in enumerate(players):
        print(f'{index + 1}. {player[0]} as {player[1]} the {player[2]} {player[3]}')
    print('-----------------------')
    return players

def exit_program():
    print("Goodbye!")
    exit()


"""Profile Menu Helpers"""

def change_level():
    print('All Characters:')
    print('-----------------------')
    chars = view_all_characters('dm')
    if len(chars) == 0:
            print("There are no characters to edit!")
            print("Returning to DM mode...")
            print('-----------------------')
            return
    else:
        print('Select a character you want to edit:')
        editing = True
        while editing:
            char_choice = input("❯❯ ")
            try:
                char_choice = int(char_choice)
                if 1 <= char_choice <= len(chars):
                    to_change = chars[char_choice - 1]
                    print('Select a new level (1-10):')
                    while True:
                        level = input("❯❯ ")
                        try:
                            level = int(level)
                            if 1 <= level <= 10:
                                print(f'★ {to_change.name} to level {level} ★')
                                print('Confirm you want to edit this character (Y/N)?')
                                choice = input("❯❯ ")
                                if choice == "Y":
                                    to_change.update_level(level)
                                    print("✔ ✔ SUCCESS ✔ ✔")
                                    print(f"{to_change.name}'s level has been changed to {level}!")
                                    print("Returning to DM mode...")
                                    print('-----------------------')
                                    editing =  False
                                    break
                                elif choice == "N":
                                    print("✖ ✖ Edit Cancelled ✖ ✖")
                                    print("Returning to DM mode...")
                                    print('-----------------------')
                                    editing =  False
                                    break
                                else:
                                    print("Type Y or N to confirm or cancel")
                            else:
                                print('Level must be between 1 and 10')
                        except ValueError:
                            print('Input must be a number')
                else:
                    print('Please select a number that matches a character')
            except ValueError:
                print('Please select by number')

def edit_active():
    next_players_names = [player[0] for player in view_players_in_next_session()]
    print('Select a player to remove from the next game:')
    while True:
        char_choice = input("❯❯ ")
        try:
            char_choice = int(char_choice)
            if 1 <= char_choice <= len(next_players_names):
                print(f'★ Remove {next_players_names[char_choice - 1]} from the next game? (Y/N) ★')
                choice = input("❯❯ ")
                if choice == "Y":
                    Player.find_by_name(next_players_names[char_choice - 1])[0].remove_active()
                    print("✔ ✔ SUCCESS ✔ ✔")
                    print(f"{next_players_names[char_choice - 1]} cancelled!")
                    print("Returning to DM Mode...")
                    print('-----------------------')
                    break
                elif choice == "N":
                    print("✖ ✖ Cancelling Cancelled ✖ ✖")
                    print("Returning to DM Mode...")
                    print('-----------------------')
                    break
                else:
                    print("Type Y or N to confirm or cancel")
            else:
                print('Please select a number that matches a character')
        except ValueError:
            print("Please select by number")
    

def view_all_characters(current_player):
    if current_player == 'dm':
        my_chars = Character.all()
    else:
        my_chars = Character.my_chars(current_player)
    for index, character in enumerate(my_chars):
        print(f'{index + 1}. {character.name} the {character.char_class} {character.race} | Level: {character.level} |')
    print('-----------------------')
    return my_chars


def delete_character(current_player):
    print('★ Delete a Character ★')
    print('-----------------------')
    my_chars = view_all_characters(current_player)
    if len(my_chars) == 0:
            print("You have no characters to delete!")
            print("Returning to your profile...")
            print('-----------------------')
            return
    else:
        print('Select which character to delete:')
        while True:
            char_choice = input("❯❯ ")
            try:
                char_choice = int(char_choice)
                if 1 <= char_choice <= len(my_chars):
                    to_delete = my_chars[char_choice - 1]
                    if to_delete.active == 1:
                        print('You cannot delete the character that is currently in use!')
                        print("If you'd like to delete this character please RSVP with a different character and try again.")
                        print("Returning to your profile...")
                        print('-----------------------')
                        break
                    else:
                        print(f'★ Delete: {to_delete.name} ★')
                        print('Confirm you want to delete this character (Y/N)?')
                        choice = input("❯❯ ")
                        if choice == "Y":
                            to_delete.delete_char()
                            print("✔ ✔ SUCCESS ✔ ✔")
                            print(f"{to_delete.name} has been deleted!")
                            print("Returning to your profile...")
                            print('-----------------------')
                            break
                        elif choice == "N":
                            print("✖ ✖ Delete Cancelled ✖ ✖")
                            print("Returning to your profile")
                            print('-----------------------')
                            break
                        else:
                            print("Type Y or N to confirm or cancel")
                else:
                    print('Please select a number that matches a character')
            except ValueError:
                print("Please select by number")

def delete_player(current_player):
    print("Delete Current Player")
    print("NOTE: THIS WILL ALSO DELETE ALL CHARACTERS BELONGING TO THIS PLAYER")
    print("Are you sure you want to continue? (Y/N)")
    while True:
        choice = input("❯❯ ")
        if choice == "Y":
            print("Are you sure?!? This CANNOT be undone! (Y/N)")
            choice = input("❯❯ ")
            if choice == "Y":
                current_player.delete()
                print("✔ ✔ SUCCESS ✔ ✔")
                print(f"{current_player.name} has been deleted!")
                print("Returning to main menu...")
                print('-----------------------')
                return True
            elif choice == "N":
                print('Player Deletion Cancelled')
                print("Returning to your profile...")
                print('-----------------------')
                break
            else:
                print('Type Y or N to confirm or cancel')
        elif choice == "N":
            print('Player Deletion Cancelled')
            print("Returning to your profile...")
            print('-----------------------')
            break
        else:
            print('Type Y or N to confirm or cancel')

def get_active_char(current_player):
    active_tuple = current_player.active_char()
    if active_tuple:
        active_character = Character.dnd_data(active_tuple)
        print(f'☺ {active_character.name}\'s Character Sheet ☺')
        print('-----------------------')
        print(f'→ Class: {active_character.char_class}')
        print(f'→ Race: {active_character.race}')
        print(f'→ Level: {active_character.level}')
        print(f'→ Alignment: {active_character.alignment}')
        print('→ Ability Stats:')
        print(f'    • Strength: {active_character.strength}')
        print(f'    • Dexterity: {active_character.dexterity}')
        print(f'    • Constitution: {active_character.constitution}')
        print(f'    • Intelligence: {active_character.intelligence}')
        print(f'    • Wisdom: {active_character.wisdom}')
        print(f'    • Charisma: {active_character.charisma}')
        print('-----------------------')
        input(f'❯❯ Press Enter to return to your profile')
    else:
        print('You do not have current character!')
        print('RSVP for the next session to set an current character.')
        print('Returning to your profile...')
        print('-----------------------')

def rsvp(current_player):
    print("★ RSVP ★")
    print('-----------------------')
    my_chars = view_all_characters(current_player)
    if len(my_chars) == 0:
            print("You must create a character before youcan  RSVP")
            print("Returning to your profile...")
            print('-----------------------')
            return
    else:
        print('Select which character you will be playing next session:')
    while True:
        char_choice = input("❯❯ ")
        try:
            char_choice = int(char_choice)
            if 1 <= char_choice <= len(my_chars):
                print(f'★ You chose: {my_chars[char_choice - 1].name} ★')
                print('Confirm your character (Y/N)?')
                choice = input("❯❯ ")
                if choice == "Y":
                    my_chars[char_choice - 1].update_active()
                    print("✔ ✔ SUCCESS ✔ ✔")
                    print("See you next session!")
                    print("Returning to your profile...")
                    print('-----------------------')
                    break
                elif choice == "N":
                    print("✖ ✖ RSVP Cancelled ✖ ✖")
                    print("Returning to your profile...")
                    print('-----------------------')
                    break
                else:
                    print("Type Y or N to confirm or cancel")
            else:
                print('Please select a number that matches a character')
        except ValueError:
            print("Please select by number")

def cancel_game():
    print('Are you sure you want to cancel your upcoming game? (Y/N)')
    while True:
        choice = input("❯❯ ")
        if choice == "Y":
            Character.cancel_game()
            print("✔ ✔ SUCCESS ✔ ✔")
            print("Upcoming game cancelled!")
            print("Returning to DM Menu...")
            print('-----------------------')
            break
        elif choice == "N":
            print("✖ ✖ Cancel Cancelled ✖ ✖")
            print("Returning to DM Menu...")
            print('-----------------------')
            break
        else:
            print("Type Y or N to confirm or cancel")