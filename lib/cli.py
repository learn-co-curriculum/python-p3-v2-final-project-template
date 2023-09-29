# main.py
from models.character import Character
from models.player import Player
from models.monster import Monster, remove_monster, attack, select_random_monster
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
        monster = select_random_monster(conn)
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

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS players (
                   id INTEGER PRIMARY KEY,
                   username TEXT, email TEXT)""")
    conn.commit()

    while True:
        print("\nChoose a scenario:")
        print("1. Scenario One")
        print("2. Scenario Two")
        print("3. Exit")

        scenario_choice = input("Choose an option: ")

        if scenario_choice == "3":
            print("Thanks for playing!")
            break

        # Taking user's name input
        player_username = input("Enter a username: ")
        player_email = input("Enter your email: ")
        player = Player(player_username, player_email)

        cursor.execute("""INSERT INTO players (username, email) VALUES (?, ?)""", (player_username, player_email))
        conn.commit()

        print(f"Welcome, {player_username}! Good luck on your adventure!")

        # Call play_scenario
        play_again = play_scenario(character, conn)
        if not play_again:
            print("Thanks for playing! See you next time.")
            break

    conn.close()


if __name__ == "__main__":
    main()
