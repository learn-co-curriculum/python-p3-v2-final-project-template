from xml.sax import make_parser
from models.__init__ import CURSOR, CONN
from models.player import Player
import re
from models.__init__ import sqlite3
class Character:
    all = {}

    available_characters = [
        {
            "Name": "Wizard",
            "XP": 0,
            "HP": 60,
            "MP": 150,
            "Description": "The classic master of arcane magic."
        },
        {
            "Name": "Fighter",
            "XP": 0,
            "HP": 120,
            "MP": 0,
            "Description": "A versatile, melee warrior that specializes in weapons and armor."
            },
        {
            "Name": "Ranger",
            "XP": 0,
            "HP": 100,
            "MP": 30,
            "Description": "Both a hunter and a tracker with great survival skills and nature magic."
        },
        {
            "Name": "Rogue",
            "XP": 0,
            "HP": 80,
            "MP": 0,
            "Description": "An expert in stealth, precision, and cunning."
        },
        {
            "Name": "Paladin",
            "XP": 0,
            "HP": 100,
            "MP": 30,
            "Description": "A holy knight with melee skills and magical abilities."
        },
        {
            "Name": "Bard",
            "XP": 0,
            "HP": 80,
            "MP": 60,
            "Description": "A jack of many trades that uses performance skills and magic."
        },

    ]

    def __init__(self, name, xp, hp, mp, player_id, id=None):
        self.id = id
        self.name = name
        self.xp = xp
        self.hp = hp
        self.mp = mp
        self.player_id = player_id

    def __repr__(self):
        player = Player.find_by_id(self.player_id)
        player_username = player.username if player else "None"
        return (
            f"<Character {self.id}: {self.name}, "
            f"Class: {self.character_class}, "
            f"HP: {self.hp}, "
            f"Level: {self.level}, "
            f"Experience: {self.xp}, "
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

        if not re.match("^[a-zA-Z_]*$", name):
            raise ValueError(
                "The character's name can only contain letters and underscores."
                )

        if not name[0].isalpha():
            raise ValueError(
                "The character's name must start with an alphabetic letter."
                )

        if not self.is_name_unique(name):
            raise ValueError("The character name must be unique.")

        self._name = name

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
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self, mp):
        if isinstance(mp, int) and mp >= 0:
            self._mp = mp
        else:
            raise ValueError("MP must be a positive integer.")

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        if isinstance(hp, int) and hp >= 0:
            self._hp = hp
        else:
            raise ValueError("HP must be a positive integer.")

    @property
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self, hp):
        if isinstance(mp, int) and mp >= 0:
            self._mp = mp
        else:
            raise ValueError("MP must be a positive integer.")

    @property
    def player_id(self):
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        # Validation can go here
        self._player_id = player_id

    @classmethod
    def create_table(cls):
        # SQL command to create Character table
        pass

    @classmethod
    def drop_table(cls):
        # SQL command to drop Character table
        pass

    def save(self):
        # Save character instance to database
        pass

    def update(self):
        # Update this character's data
        pass

    def delete(self):
        # Delete this character from database
        pass

    @classmethod
    def create(cls, name, player_id):
        # Create and return a new character instance
        pass

    @classmethod
    def instance_from_db(cls, row):
        # Initialize an instance from a database row
        pass

    @classmethod
    def get_all(cls):
        # Get all character instances
        pass

    @classmethod
    def find_by_id(cls, id):
        # Find a character by their ID
        pass

    @classmethod
    def find_by_name(cls, name):
        # Find a character by their name
        pass

    @classmethod
    def is_name_unique(cls, name):
        # Search in db or in-memory
        # if a result, return False
        # else: return True
        pass
