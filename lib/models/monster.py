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
