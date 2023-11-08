import random
from models.characters import Character

character_info = {
    'name': '',
    'class': '',
    'race': '',
    'alignment': '',
    'abilities': '',
    'level': '',
    'player_id': ''
}

states = ['name', 'class', 'race', 'alignment', 'abilities', 'level']

def create_new_char_menu(current_player):
    character_info['player_id'] = current_player.id
    creating = True
    while creating:
        current_state = 'name'

        while current_state:
            if current_state == 'name':
                print("Create a name:")
                get_name()
                current_state = 'class'
            elif current_state == 'class':
                print('Select a class:')
                get_class()
                current_state = 'race'
            elif current_state == 'race':
                print('Select a race:')
                get_race()
                current_state = 'alignment'
            elif current_state == 'alignment':
                print("Select an alignment:")
                get_alignment()
                current_state = 'abilities'
            elif current_state == 'abilities':
                print("Ability Stats:")
                get_abilities()
                current_state = 'level'
            elif current_state == 'level':
                print("What level is your character?")
                get_level()
                current_state = None
        print(f'☺ {character_info["name"]}\'s Character Sheet ☺')
        print('-----------------------')
        print(f'→ Class: {character_info["class"]}')
        print(f'→ Race: {character_info["race"]}')
        print(f'→ Level: {character_info["level"]}')
        print(f'→ Alignment: {character_info["alignment"]}')
        print('→ Ability Stats:')
        for ability, score in character_info["abilities"].items():
            print(f'    • {ability}: {score}')
        print('-----------------------')
        while True:
            print("Confirm your new character (Y/N)?")
            choice = input("❯❯ ")
            if choice == "Y":
                Character.create_char(
                    character_info["name"],
                    character_info["class"],
                    character_info["race"],
                    character_info["abilities"]["Strength"],
                    character_info["abilities"]["Dexterity"],
                    character_info["abilities"]["Constitution"],
                    character_info["abilities"]["Intelligence"],
                    character_info["abilities"]["Wisdom"],
                    character_info["abilities"]["Charisma"],
                    character_info["alignment"],
                    character_info["player_id"],
                    character_info['level']
                )
                print("✔ ✔ SUCCESS ✔ ✔")
                print("Your new character has been saved!")
                print("Returning to your profile...")
                return
            elif choice == "N":
                print("✖ ✖ CANCELLED ✖ ✖")
                print("Returning to your Profile...")
                creating = False
                break
            else:
                print("Type Y or N to confirm or restart your new character")
        


def get_name():
    while True:
        name = input("❯❯ ")
        if 3 <= len(name) <= 20:
            character_info["name"] = name
            print(f'★ Character\'s name: {character_info["name"]} ★')
            break
        else:
            print('The name must be 3-20 characters long.')

def get_class():
    while True:
        classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
        for i, class_name in enumerate(classes, 1):
            print(f"{i}. {class_name}")
        
        choice = input('❯❯ ')
        try:
            choice = int(choice)
            if 1 <= choice <= len(classes):
                character_info["class"] = classes[choice - 1]
                print(f'★ You chose: {character_info["class"]} ★')
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please select by number")


def get_race():
    while True:
        races = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Goblin", "Halfling", "Human", "Orc", "Tiefling"]
        for i, race in enumerate(races, 1):
            print(f"{i}. {race}")

        choice = input('❯❯ ')
        try:
            choice = int(choice)
            if 1 <= choice <= len(races):
                character_info["race"] = races[choice - 1]
                print(f'★ You chose: {character_info["race"]} ★')
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please select by number.")

""" creates an even grid of alignments using left-justify at a width of the max char length of alignment strs. prompts users to select alignment using rows and columns as indices, row being the different lists of alignments and columns being the alignments in each list
"""
def get_alignment():
    alignments = [
        ["Lawful Good", "Lawful Neutral", "Lawful Evil"],
        ["Neutral Good", "True Neutral", "Neutral Evil"],
        ["Chaotic Good", "Chaotic Neutral", "Chaotic Evil"]
        ]
    max_length = max(len(alignment) for row in alignments for alignment in row)
    for row in alignments:
        alignment_row = "| " + " | ".join(alignment.ljust(max_length) for alignment in row) + " |"
        print(alignment_row)
    while True:
        # row_choice = int(input('❯❯ Enter the row number: ')) - 1
        row_choice = input('❯❯ Enter the row number: ')
        try:
            row_choice = int(row_choice) - 1
            if 0 <= row_choice < 3:
                while True:
                    # col_choice = int(input('❯❯ Enter the column number: ')) - 1
                    col_choice = input('❯❯ Enter the column number: ')
                    try:
                        col_choice = int(col_choice) - 1
                        if 0 <= col_choice < 3:
                            alignment = alignments[row_choice][col_choice]
                            character_info['alignment'] = alignment
                            print(f'★ You chose: {character_info["alignment"]} ★')
                            break
                        else:
                            print("Invalid choice. Please try again.")
                    except ValueError:
                        print("Must be a valid number.")
                break
            else:
                    print("Invalid choice. Please try again.")
        except ValueError:
            print("Must be a valid number.")


"""returns a list of 3 random numbers between 1-6. adds the 3 numbers and assigns it to a variable 'ability score'
"""
def roll_3d6():
    print('-----------------------')
    print("Rolling 3 d6...")
    dice_rolls = [random.randint(1, 6) for _ in range(3)]
    print(f"Dice results: {dice_rolls}")
    ability_score = sum(dice_rolls)
    return ability_score

"""returns the list of abilities, user can select an ability and invoke roll_3d6. adds ability: score pair to dictionary and removes ability from list of abilities. loops until ability list is empty 
"""
def get_abilities():
    abilities = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
    ability_scores = {}
    for i, ability in enumerate(abilities, 1):
        print(f"{i}. {ability}")
    while abilities:
        selected_ability = abilities.pop(0)
        input(f'❯❯ Press Enter to roll for {selected_ability}')
        ability_scores[selected_ability] = roll_3d6()
        print(f'★ {selected_ability} Score: {ability_scores[selected_ability]} ★')
        print('-----------------------')

    character_info["abilities"] = ability_scores
    
def get_level():
    set_level = True
    while set_level:
        level = input('❯❯ ')
        try:
            int_level = int(level)
            if 1 <= int_level <= 10:
                character_info["level"] = int_level
                set_level = False
                break
            else: 
                print('Level must be between 1 and 10')
        except ValueError:
            print("Level must be a number.")