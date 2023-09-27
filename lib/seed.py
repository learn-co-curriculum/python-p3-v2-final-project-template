#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.itinerary import Trip, Activity


def seed_database():
    Trip.drop_table()
    Trip.create_table()

    Activity.drop_table()
    Activity.create_table()

    summer = Trip.create("Summer Break", "Cancun")
    swimming = Activity.create(
        "Swimming", "Swimming in pool", 9.00, "Thursday", 1)


seed_database()
print("Seeded database")
