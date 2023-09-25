# lib/models/department.py
from models.__init__ import CURSOR, CONN


class Trip:
    def __init__(self, day, trip, id=None):
        self.day = day
        self.trip = trip
        self.id = id


class Activity:
    def __init__(self, activity, description, price):
        self.activity = activity
        self.description = description
        self.price = price

    @property
    def activity(self):
        return self._activity

    @activity.setter
    def activity(self, activity):
        if isinstance(activity, str) and len(activity) in range(1, 25):
            self._activity = activity
        else:
            raise Exception("Activity must be a string.")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if isinstance(description, str) and len(description) > 0:
            self._description = description
        else:
            raise Exception("Invalid description.")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, float):
            self._price = price
        else:
            raise Exception("Invalid price.")
