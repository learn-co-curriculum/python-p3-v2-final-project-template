from models.__init__ import CURSOR, CONN
from models.player import Player
import re
import sqlite3


class Character:
    ALL = {}

    available_characters = [
        {
            "Class": "Wizard",
            "XP": 0,
            "hp": 60,
            "MP": 150,
            "Description": "The classic master of arcane magic."
        },
        {
            "Class": "Fighter",
            "XP": 0,
            "hp": 120,
            "MP": 0,
            "Description": "A versatile, melee warrior that specializes in weapons and armor."
        },
        {
            "Class": "Ranger",
            "XP": 0,
            "hp": 100,
            "MP": 30,
            "Description": "Both a hunter and a tracker with great survival skills and nature magic."
        },
        {
            "Class": "Rogue",
            "XP": 0,
            "hp": 80,
            "MP": 0,
            "Description": "An expert in stealth, precision, and cunning."
        },
        {
            "Class": "Paladin",
            "XP": 0,
            "hp": 100,
            "MP": 30,
            "Description": "A holy knight with melee skills and magical abilities."
        },
        {
            "Class": "Bard",
            "XP": 0,
            "hp": 80,
            "MP": 60,
            "Description": "A jack of many trades that uses performance skills and magic."
        },

    ]

    def __init__(self, name, character_class, xp, hp, mp, player_id, id=None):
        self.id = id
        self.name = name
        self._character_class = character_class
        self.xp = xp
        self.hp = hp
        self.mp = mp
        self.player_id = player_id
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def use_healing_item(self):
        if "Healing Item" in self.inventory:
            self.hp += 30
            self.inventory.remove("Healing Item")
            print(f"{self.name} used a Healing Item and restored 30 HP!")

    def __repr__(self):
        player = Player.find_by_id(self.player_id)
        player_username = player.name if player else "None"
        return (
            f"<Character {self.id}: {self.name}, "
            f"Class: {self.character_class}, "
            f"XP: {self.xp}, "
            f"hp: {self.hp}, "
            f"MP: {self.mp}, "
            f"Owned by: {player_username} with id: {self.player_id}>"
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("The character name must be a string.")

        if not 3 <= len(name) <= 20:
            raise ValueError(
                "The character name's length must be between 3 and 20 characters."
            )

        if not name[0].isalpha():
            raise ValueError(
                "The character's name must start with an alphabetic letter."
            )

        if not re.match("^[a-zA-Z_]*$", name):
            raise ValueError(
                "The character's name can only contain letters and underscores."
            )

        if not self.is_username_unique(name):
            raise ValueError("The character name must be unique.")

        self._name = name

    @property
    def character_class(self):
        return self._character_class

    @character_class.setter
    def character_class(self, character_class):
        if isinstance(character_class, str):
            self._character_class = character_class
        else:
            raise ValueError("Character class must be a string.")

    @property
    def xp(self):
        return self._xp

    @xp.setter
    def xp(self, xp):
        if isinstance(xp, int) and xp >= 0:
            self._xp = xp
        else:
            raise ValueError("XP must be a positive integer.")

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        if isinstance(hp, int) and hp >= 0:
            self._hp = hp
        else:
            raise ValueError("hp must be a positive integer.")

    @property
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self, mp):
        if isinstance(mp, int) and mp >= 0:
            self._mp = mp
        else:
            raise ValueError("MP must be a positive integer.")

    @property
    def player_id(self):
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        if isinstance(player_id, int) and player_id >= 0:
            self._player_id = player_id
        else:
            raise ValueError("Player Id must be a positive integer.")

    @classmethod
    def create_table(cls, conn):
        cursor = conn.cursor()
        sql = """
            CREATE TABLE IF NOT EXISTS characters (
            id INTEGER PRIMARY KEY,
            name TEXT,
            character_class TEXT,
            xp INTEGER,
            hp INTEGER,
            mp INTEGER,
            player_id INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        # SQL command to drop character table that persists Character instances
        sql = """
            DROP TABLE IF EXISTS characters;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        # Save character instance to new database row
        sql = """
            INSERT INTO characters (name, character_class, xp, hp, mp, player_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """

        # Update object id attribute using the primary key value of new row
        CURSOR.execute(sql, (
            self.name, self.character_class, self.xp, self.hp, self.mp, self.player_id
        ))
        CONN.commit()

        # Save the object in local dictionary using table row's PK as dictionary key
        self.id = CURSOR.lastrowid
        type(self).ALL[self.id] = self

    def update(self):
        # Update this character's table row corresponding to the current Character instance
        sql = """
            UPDATE characters
            SET name = ?, character_class = ?, xp = ?, hp = ?, mp = ?, player_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.character_class,
                       self.xp, self.hp, self.mp, self.player_id))
        CONN.commit()

    def delete(self):
        # Delete this character from database
        sql = """
            DELETE FROM characters
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).ALL[self.id]

        # Set id to None
        self.id = None

    @classmethod
    def create(cls, name, character_class, xp, hp, mp, player_id):
        # Create a new character instance and save it to database row
        character = cls(name, character_class, xp, hp, mp, player_id)
        character.save()
        return character

    @classmethod
    def instance_from_db(cls, row):
        # Return a character object with attributes from correct table row

        # Check the dictionary for an existing instance using the row's primary key
        character = cls.ALL.get(row[0])
        if character:
            # ensure attributes match row values in case local instance was modified
            character.name = row[1]
            character.character_class = row[2]
            character.xp = row[3]
            character.hp = row[4]
            character.mp = row[5]
            character.player_id = row[6]
        else:
            # not in dictionary, create new instance and add to dictionary
            character = cls(row[1], row[2], row[3], row[4], row[5], row[6])
            character.id = row[0]
            cls.ALL[character.id] = character
        return character

    @classmethod
    def get_all(cls):
        # Return a list containing all character instances
        sql = """
            SELECT *
            FROM characters
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        # Find a character by their ID
        sql = """
            SELECT *
            FROM characters
            WHERE id = ?
        """
        # Return Character object from the table row with matching primary key
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        # Find a character by their name
        sql = """
            SELECT *
            FROM characters
            WHERE name is ?
        """
        # Return the first table row of a Character object matching a name
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def is_username_unique(cls, name):
        # Search in-memory
        is_unique_in_memory = not any(
            character.name == name for character in cls.ALL.values())

        # Search in database
        sql = """
            SELECT *
            FROM characters
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        is_unique_in_db = row is None

        # if a result, return False; else: return True
        return is_unique_in_db and is_unique_in_memory
