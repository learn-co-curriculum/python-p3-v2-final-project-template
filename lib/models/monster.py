import sqlite3
import random


class Monster:
    # Original Monster Data
    MONSTERS_DATA = [
        ("Glowworm Guardian", 100, False),
        ("Apparition of Lady Eliza", 80, True),
        ("Frostbite", 120, True),
        ("Captain Blackbeard's Shadow", 140, False),
        ("Fireborn Drake", 160, True),
        ("Echo Harvester", 90, False),
        ("Captain Barnacle", 110, False),
        ("Sprite Sylph", 70, True),
        ("Stone Golem", 200, True),
        ("Sea Wraith", 130, False),
        ("Bog Whisperer", 95, True),
        ("Spectral Legionnaire", 150, False),
        ("Aethereal Harbinger", 170, True),
        ("Lunarchid", 80, False),
    ]

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

        # Check if the monsters already exist in the table
        existing_monsters = cursor.execute(
            'SELECT name FROM monsters').fetchall()
        existing_monsters = [monster[0] for monster in existing_monsters]

        for monster in cls.MONSTERS_DATA:
            if monster[0] not in existing_monsters:
                cursor.execute(
                    'INSERT INTO monsters (name, hit_points, has_healing_item) VALUES (?, ?, ?)', monster)
                conn.commit()

    @classmethod
    def select_random_monster(cls, conn):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM monsters')
        monsters = cursor.fetchall()
        monster_data = random.choice(monsters)
        return cls(*monster_data)

    @classmethod
    def get_monster_by_name(cls, conn, monster_name):
        sql = """
            SELECT * FROM monsters WHERE name = ?
        """
        cursor = conn.cursor()
        row = cursor.execute(sql, (monster_name,)).fetchone()
        if row:
            return cls(*row)
        else:
            print(
                f"The monster {monster_name} has been defeated previously, recreating it...")
            # Find the original monster data
            for original_monster in cls.MONSTERS_DATA:
                if original_monster[0] == monster_name:
                    cursor.execute(
                        'INSERT INTO monsters (name, hit_points, has_healing_item) VALUES (?, ?, ?)', original_monster)
                    conn.commit()
                    row = cursor.execute(sql, (monster_name,)).fetchone()
                    return cls(*row)
            # If the monster data is not found
            raise ValueError("Original monster data not found.")


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
        character.hp -= damage
        print(f"{monster.name} attacked back {character.name} for {damage} damage!")

    return character.hp <= 0
