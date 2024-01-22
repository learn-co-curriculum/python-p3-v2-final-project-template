#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.player import Player
from models.level import Level
# from models.pet import Pet

def seed_database():
    # Pet.drop_table()
    Player.drop_table()
    Level.drop_table()
    Player.create_table()
    Level.create_table()
    # Pet.create_table()

    # # Create seed data
    player1 = Player.create("Andrew")
    player2 = Player.create("Katie")
    level1 = Level.create("1-a", "Beginner", "Hello, World!")
    level2 = Level.create("1-b", "Beginner", "Practice makes perfect.")
    level3 = Level.create("1-c", "Beginner", "Keyboard ninja in training.")

seed_database()
print("Seeded database")
