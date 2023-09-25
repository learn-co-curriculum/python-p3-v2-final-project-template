#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.itinerary import Trip


def seed_database():
    Trip.drop_table()
    Trip.create_table()

    summer = Trip.create("Summer Break", "Cancun")


seed_database()
print("Seeded database")