# main.py
from models.character import Character
from models.player import Player
from models.monster import Monster, remove_monster, attack
from models.scenario import Scenario
import sqlite3

def play_scenario(character, conn):
    cursor = conn.cursor()

    for step in range(1, 6):
        print(f"\nStep {step}")

        # Assign a random scenario
        scenario = Scenario.get_random_scenarios(cursor, 1)[0]
        print(f"{scenario.name}: {scenario.description}")

        # Assign a random monster
        monster = Monster.select_random_monster(conn)

        print(f"You encounter a {monster}!")

        while monster.hit_points > 0:
            input("Press enter to attack!")
            player_defeated = attack(character, monster)

            if player_defeated:
                print(f"{character.name} has been defeated by {monster.name}!")
                return False

            if monster.hit_points <= 0:
                print(f"{monster.name} has been defeated!")
                break

    play_again = input("Scenario ended. Do you want to play again? (y/n): ").lower()
    return play_again == 'y'

def main():
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()

    Character.create_table(conn)

    while True:
        print("\nChoose a character:")
        for index, char_info in enumerate(Character.available_characters, 1):
            print(f"{index}. {char_info['Class']} - {char_info['Description']}")

        valid_characters = [str(i) for i in range(1, len(Character.available_characters) + 1)]
        valid_characters.append("exit")

        while True:
            character_choice = input("Choose a character (1-6 or type 'exit' to quit): ").lower()

            if character_choice in valid_characters:
                break
            else:
                print("Invalid input! Please select a valid number or type 'exit'.")

        if character_choice == "exit":
            print("You chose to exit. Goodbye!")
            conn.close()
            exit()

        character_info = Character.available_characters[int(character_choice) - 1]

        # Taking user's name input
        player_username = input("Enter a username: ")
        player_email = input("Enter your email: ")
        player = Player.create(player_username, player_email)

        # Create Character
        character_name = input("Enter a name for your character: ")
        character = Character.create(character_name, character_info['Class'], character_info['XP'],
                                      character_info['hp'], character_info['MP'], player.id)

        print(f"Welcome, {character_name} the {character.character_class}! Good luck on your adventure!")

        # Call play_scenario
        play_again = play_scenario(character, conn)
        if not play_again:
            print("Thanks for playing! See you next time.")
            break

    conn.close()

if __name__ == "__main__":
    main()
