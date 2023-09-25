# lib/models/department.py
from models.__init__ import CURSOR, CONN

class Trip:
    def __init__(self, day, trip, id=None):
        self.day = day
        self.trip = trip
        self.id = id
