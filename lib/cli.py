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

        # Extract the monster name from the scenario description
        monster_name = next(
            (monster_data[0] for monster_data in Monster.MONSTERS_DATA if monster_data[0] in scenario.description), None)

        if not monster_name:
            print("No matching monster found for the scenario. Skipping to next step.")
            continue

        # Fetch the monster associated with the scenario using monster name
        monster = Monster.get_monster_by_name(conn, monster_name)

        # Check if monster is not None before proceeding
        if monster is None:
            print("No monster found in the database. Skipping to next step.")
            continue

        print(f"You encounter a {monster.name}!")

        while monster.hit_points > 0:
            if "Healing Item" in character.inventory:
                use_item = input(
                    "You have a Healing Item! Do you want to use it? (y/n): ").lower()
                if use_item == 'y':
                    character.use_healing_item()

            # Provide the user with an option to either attack or check their HP
            action = input("Press 1 to attack or 2 to check your HP: ")

            if action == "2":
                print(f"Your current HP is {character.hp}")
                continue  # Skip the rest of the loop, prompting the user again

            elif action == "1":
                player_defeated = attack(character, monster)

            if player_defeated:
                print(f"{character.name} has been defeated by {monster.name}!")
                character.delete(cursor, conn)
                return False

            if monster.hit_points <= 0:
                print(f"{monster.name} has been defeated!")
                remove_monster(cursor, monster.id)
                conn.commit()
                if monster.has_healing_item and not monster.healing_item_used:
                    character.add_to_inventory("Healing Item")
                    print("You have found a Healing Item!")
                break

    play_again = input(
        "Scenario ended. Do you want to play again? (y/n): ").lower()
    return play_again == 'y'


def main():
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()

    Character.create_table(conn)
    Monster.initialize_monsters(conn)
    Scenario.initialize_scenario(conn)

    while True:
        print("\nChoose a character:")
        for index, char_info in enumerate(Character.available_characters, 1):
            print(
                f"{index}. {char_info['Class']} - {char_info['Description']}")

        valid_characters = [str(i) for i in range(
            1, len(Character.available_characters) + 1)]
        valid_characters.append("exit")

        while True:
            character_choice = input(
                "Choose a character (1-6 or type 'exit' to quit): ").lower()

            if character_choice in valid_characters:
                break
            else:
                print("Invalid input! Please select a valid number or type 'exit'.")

        if character_choice == "exit":
            print("You chose to exit. Goodbye!")
            conn.close()
            exit()

        character_info = Character.available_characters[int(
            character_choice) - 1]

        # Taking user's name input
        player_username = input("Enter a username: ")
        player_email = input("Enter your email: ")
        player = Player.create(player_username, player_email)

        # Create Character
        character_name = input("Enter a name for your character: ")
        character = Character.create(character_name, character_info['Class'], character_info['XP'],
                                     character_info['hp'], character_info['MP'], player.id)

        print(
            f"Welcome, {character_name} the {character.character_class}! Good luck on your adventure!")

        # Call play_scenario
        play_again = play_scenario(character, conn)
        if not play_again:
            print("Thanks for playing! See you next time.")
            break

    conn.close()


if __name__ == "__main__":
    main()
