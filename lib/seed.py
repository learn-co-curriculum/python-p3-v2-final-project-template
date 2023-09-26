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
        "Swimming", "Swimming at the Infinity Pool", 0.00, "Thursday", summer.id)


seed_database()
print("Seeded database")
