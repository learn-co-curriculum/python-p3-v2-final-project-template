import sqlite3
import random
from models.monster import Monster, select_random_monster, remove_monster, attack
from models.player import Player


def main():
    conn = sqlite3.connect('game.db')

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

        print(f"Welcome, {player_username}! Good luck on your adventure!")

        for step in range(1, 6):
            print(f"\nStep {step}")
            player_defeated = False

            if step in [2, 4]:
                current_monster = select_random_monster(conn)
                print(f"A wild {current_monster} has appeared!")

            elif step == 5:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT * FROM monsters WHERE name IN ('Mothra', 'Godzilla')")
                big_monsters = cursor.fetchall()

                if not any(monster[1] == 'Mothra' for monster in big_monsters):
                    cursor.execute(
                        "INSERT INTO monsters (name, hit_points) VALUES ('Mothra', 175)")
                if not any(monster[1] == 'Godzilla' for monster in big_monsters):
                    cursor.execute(
                        "INSERT INTO monsters (name, hit_points) VALUES ('Godzilla', 175)")

                conn.commit()

                current_monster = Monster(
                    *random.choice([monster for monster in big_monsters if monster[1] in ['Mothra', 'Godzilla']]))
                print(f"A wild {current_monster} has appeared!")

            else:
                print("No monster appeared at this step.")
                input("Press Enter to continue to the next step...")
                continue

            while current_monster.hit_points > 0:
                print(f"\n1. Attack the {current_monster.name}")
                print("2. Show your status")

                if current_monster.has_healing_item and not current_monster.healing_item_used:
                    print("3. Use healing item")

                choice = input("Choose an option: ")

                if choice == "1":
                    player_defeated = attack(player, current_monster)

                    if current_monster.hit_points <= 0:
                        print(f"{current_monster.name} has been defeated!")
                        remove_monster(conn, current_monster)
                        if current_monster.has_healing_item:
                            print(
                                f"{current_monster.name} was carrying a healing item!")
                    if player_defeated:
                        print("You have been defeated!")
                        break

                elif choice == "2":
                    print(player)

                elif choice == "3" and current_monster.has_healing_item and not current_monster.healing_item_used:
                    healing_amount = 30
                    player.hit_points = min(
                        player.hit_points + healing_amount, player.max_hit_points)
                    current_monster.healing_item_used = True
                    print(
                        f"You used the healing item and restored {healing_amount} HP!")

            if player_defeated:
                break

            input("Press Enter to continue to the next step...")

        play_again = input(
            "Scenario ended. Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! See you next time.")
            break

    conn.close()


if __name__ == "__main__":
    main()
