import sqlite3
import random

class Monster:
    def __init__(self, id, name, hit_points, has_healing_item):
        self.id = id
        self.name = name
        self.hit_points = hit_points
        self.has_healing_item = has_healing_item
        self.healing_item_used = False

    def __repr__(self):
        return f"{self.name} (HP: {self.hit_points})"

    @classmethod
    def initialize_monsters(cls, conn):
        cursor = conn.cursor()
        sql = """
            CREATE TABLE IF NOT EXISTS monsters (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                hit_points INTEGER NOT NULL,
                has_healing_item BOOLEAN NOT NULL DEFAULT FALSE
            )
        """
        cursor.execute(sql)
        conn.commit()

        # Define monsters
        monsters_data = [
            ("Wolf", 75, True),
            ("Orc", 125, False),
            ("Spooky Skeleton", 85, True),
            ("Silver wolf", 65, False),
            ("Drunken man", 90, True),
            ("Cunning witch", 85, True),
            ("Large spider", 100, False),
        ]

        # Check if the monsters already exist in the table
        existing_monsters = cursor.execute('SELECT name FROM monsters').fetchall()
        existing_monsters = [monster[0] for monster in existing_monsters]

        for monster in monsters_data:
            if monster[0] not in existing_monsters:
                cursor.execute('INSERT INTO monsters (name, hit_points, has_healing_item) VALUES (?, ?, ?)', monster)
                conn.commit()

    @classmethod
    def select_random_monster(cls, conn):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM monsters')
        monsters = cursor.fetchall()
        monster_data = random.choice(monsters)
        return cls(*monster_data)


def remove_monster(conn, monster):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM monsters WHERE id = ?', (monster.id,))
    conn.commit()


def attack(character, monster):
    damage = 10
    monster.hit_points -= damage
    print(f"{character.name} attacked {monster.name} for {damage} damage!")

    if random.choice([True, False]):
        damage = 5
        character.hit_points -= damage
        print(f"{monster.name} attacked back {character.name} for {damage} damage!")

    return character.hit_points <= 0
