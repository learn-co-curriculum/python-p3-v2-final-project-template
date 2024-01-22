#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.player import Player
# from models.pet import Pet

def seed_database():
    # Pet.drop_table()
    Player.drop_table()
    Player.create_table()
    # Pet.create_table()

    # # Create seed data
    player1 = Player.create("Andrew")
    player2 = Player.create("Katie")
    # Pet.create("Brutus", "dog", 1, 1)
    # Pet.create("Citrus", "cat", 1, 2)

seed_database()
print("Seeded database")
