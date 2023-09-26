import sqlite3
import random
from models.character import Character
from models.player import Player

class Monster:
    def __init__(self, id, name, hit_points, has_healing_item):
        self.id = id
        self.name = name
        self.hit_points = hit_points
        self.has_healing_item = has_healing_item
        self.healing_item_used = False

    def __repr__(self):
        return f"{self.name} (HP: {self.hit_points})"


# class Player:
#     def __init__(self, name, hit_points=100):
#         self.name = name
#         self.hit_points = hit_points
#         self.max_hit_points = 100

#     def __repr__(self):
#         return f"{self.name} (HP: {self.hit_points})"


def select_random_monster(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM monsters')
    monsters = cursor.fetchall()
    monster = random.choice(monsters)
    return Monster(*monster)


def remove_monster(conn, monster):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM monsters WHERE id = ?', (monster.id,))
    conn.commit()


def attack(player, monster):
    damage = 10
    monster.hit_points -= damage
    print(f"{player.name} attacked {monster.name} for {damage} damage!")

    if random.choice([True, False]):
        damage = 5
        player.hit_points -= damage
        print(f"{monster.name} attacked back {player.name} for {damage} damage!")

    return player.hit_points <= 0


# def main():
#     conn = sqlite3.connect('game.db')

#     while True:
#         print("Choose a scenario:")
#         print("1. Scenario One")
#         print("2. Scenario Two")
#         print("3. Exit")

#         scenario_choice = input("Choose an option: ")

#         if scenario_choice == "3":
#             break

#         player = Player("Hero")

#         for step in range(1, 6):
#             print(f"\nStep {step}")
#             player_defeated = False

#             if step in [2, 4]:
#                 current_monster = select_random_monster(conn)
#                 print(f"A wild {current_monster} has appeared!")

#             elif step == 5:
#                 cursor = conn.cursor()
#                 cursor.execute("SELECT * FROM monsters WHERE name IN ('Mothra', 'Godzilla')")
#                 big_monsters = cursor.fetchall()

#                 if not any(monster[1] == 'Mothra' for monster in big_monsters):
#                     cursor.execute("INSERT INTO monsters (name, hit_points) VALUES ('Mothra', 175)")
#                 if not any(monster[1] == 'Godzilla' for monster in big_monsters):
#                     cursor.execute("INSERT INTO monsters (name, hit_points) VALUES ('Godzilla', 175)")

#                 conn.commit()

#                 current_monster = Monster(*random.choice([monster for monster in big_monsters if monster[1] in ['Mothra', 'Godzilla']]))
#                 print(f"A wild {current_monster} has appeared!")

#             else:
#                 print("No monster appeared at this step.")
#                 input("Press Enter to continue to the next step...")
#                 continue

#             while current_monster.hit_points > 0:
#                 print(f"\n1. Attack the {current_monster.name}")
#                 print("2. Show your status")
#                 print("3. Run away")

#                 if current_monster.has_healing_item and not current_monster.healing_item_used:
#                     print("4. Use healing item")

#                 choice = input("Choose an option: ")

#                 if choice == "1":
#                     player_defeated = attack(player, current_monster)

#                     if current_monster.hit_points <= 0:
#                         print(f"{current_monster.name} has been defeated!")
#                         remove_monster(conn, current_monster)
#                         if current_monster.has_healing_item:
#                             print(f"{current_monster.name} was carrying a healing item!")
#                     if player_defeated:
#                         print("You have been defeated!")
#                         break

#                 elif choice == "2":
#                     print(player)

#                 elif choice == "3":
#                     print("You ran away!")
#                     break

#                 elif choice == "4" and current_monster.has_healing_item and not current_monster.healing_item_used:
#                     healing_amount = 30
#                     player.hit_points = min(player.hit_points + healing_amount, player.max_hit_points)
#                     current_monster.healing_item_used = True
#                     print(f"You used the healing item and restored {healing_amount} HP!")

#             if player_defeated:
#                 break

#             input("Press Enter to continue to the next step...")

#         play_again = input("Scenario ended. Do you want to play again? (y/n): ").lower()
#         if play_again != 'y':
#             break

#     conn.close()


# if __name__ == "__main__":
#     main()

