import random

character_info = {
    'name': '',
    'class': '',
    'race': '',
    'alignment': '',
    'abilities': ''
}

states = ['name', 'class', 'race', 'alignment', 'abilities']

def create_new_char_menu():
    while True:
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
                current_state = None
    
    
        print(f'☺ {character_info["name"]}\'s Character Sheet ☺')
        print(f'→ Class: {character_info["class"]}')
        print(f'→ Race: {character_info["race"]}')
        print(f'→ Alignment: {character_info["alignment"]}')
        print('→ Ability Stats:')
        for ability, score in character_info["abilities"].items():
            print(f'    • {ability}: {score}')
        print("Confirm your new character (Y/N)?")
        choice = input("> ")
        if choice == "Y":
            print("✔ ✔ SUCCESS ✔ ✔")
            print("Your new character has been saved!")
            print("Returning to your profile...")
            break
        elif choice == "N":
            print("✖ ✖ CANCELLED ✖ ✖")
            print("Restarting Character Form...")
        else:
            print("Type Y or N to confirm or restart your new character")
        current_state = 'name'


def get_name():
    name = input("❯❯ ")
    if 3 <= len(name) <= 20:
        character_info["name"] = name
        print(f'★ Character\'s name: {character_info["name"]} ★')
    else:
        print('The name must be 3-20 characters long.')

def get_class():
    classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    
    for i, class_name in enumerate(classes, 1):
        print(f"{i}. {class_name}")
    choice = int(input('❯❯ '))
    if 1 <= choice <= len(classes):
        character_info["class"] = classes[choice - 1]
        print(f'★ You chose: {character_info["class"]} ★')
    else:
        print("Invalid choice. Please try again.")


def get_race():
    races = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Goblin", "Halfling", "Human", "Orc", "Tiefling"]
    for i, race in enumerate(races, 1):
        print(f"{i}. {race}")
    choice = int(input('❯❯ '))
    if 1 <= choice <= len(races):
        character_info["race"] = races[choice - 1]
        print(f'★ You chose: {character_info["race"]} ★')
    else:
        print("Invalid choice. Please try again.")

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
    
    row_choice = int(input('❯❯ Enter the row number: ')) - 1
    col_choice = int(input('❯❯ Enter the column number: ')) - 1
    if 0 <= row_choice < 3 and 0 <= col_choice < 3:
        alignment = alignments[row_choice][col_choice]
        character_info['alignment'] = alignment
        print(f'★ You chose: {character_info["alignment"]} ★')
    else:
        print("Invalid choice. Please try again.")

"""returns a list of 3 random numbers between 1-6. adds the 3 numbers and assigns it to a variable 'ability score'
"""
def roll_3d6():
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
    while abilities:
        print("Roll for: ")
        for i, ability in enumerate(abilities, 1):
            print(f"{i}. {ability}")
        choice = int(input('❯❯ '))
        if 1 <= choice <= len(abilities):
            selected_ability = abilities.pop(choice - 1)
            input(f'❯❯ Press Enter to roll for {selected_ability}')
            ability_scores[selected_ability] = roll_3d6()
            print(f'★ {selected_ability} Score: {ability_scores[selected_ability]} ★')
        else:
            print("Invalid choice. Please try again.")
    print(f'★ {character_info["name"]}\'s Ability Stats ★')
    character_info["abilities"] = ability_scores
    for ability, score in ability_scores.items():
        print(f'{ability}: {score}')

