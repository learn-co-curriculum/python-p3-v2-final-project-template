# lib/models/department.py
from models.__init__ import CURSOR, CONN


class Trip:
    def __init__(self, day, trip, id=None,):
        self.day = day
        self.trip = trip
        self.id = id
        

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day):
        if isinstance(day, str):
            self._day = day
        else:
            raise Exception("Day must be a string that is a weekday")

    @property
    def trip(self):
        return self._trip

    @trip.setter
    def trip(self, trip):
        if isinstance(trip, str) and len(trip) > 3 and not hasattr(self, "trip"):
            self._trip = trip
        else:
            raise Exception("Trip must be unique string over 3 characters")

    @property
    def activity(self):
        return self._activity

        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS trips (
            id INTEGER PRIMARY KEY,
            name TEXT,      
            location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS trips;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO trips (day, trip, activity)
            VALUES(?,?)
        """

        CURSOR.execute(sql(self.day, self.trip))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, day, trip): 
        trip = cls(day, trip)
        trip.save()
        return trip

class Activity:
    def __init__(self, activity, description, price, id=None):
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

    def create_activity():
        activity = input("Enter activity: ")
        description = input("Enter description: ")
        try:
            price = float(input("Enter price: "))
        except ValueError:
            print("Invalid price. Please enter a valid price.")
            return None

        try:
            activity = Activity(activity, description, price)
            return activity
        except ValueError as e:
            print(str(e))
            return None
