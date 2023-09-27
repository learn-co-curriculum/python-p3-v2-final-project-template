# lib/models/itinerary.py
from models.__init__ import CURSOR, CONN


class Trip:

    all = {}

    def __init__(self, name, location, id=None,):
        self.name = name
        self.location = location
        self.id = id

    def __repr__(self):
        return f"\033[36m<Trip {self.id}: {self.name}, {self.location}>\033[0m"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) in range(3, 31):
            self._name = name
        else:
            raise Exception(
                "Trip name must be unique string between 3-30 characters.")

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        if isinstance(location, str) and len(location) > 3:
            self._location = location
        else:
            raise Exception("Location must be a string over 3 characters")

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
            INSERT INTO trips (name, location)
            VALUES(?,?)
        """

        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, location):
        trip = cls(name, location)
        trip.save()
        return trip

    def update(self):
        """Update the table row corresponding to the current Trip instance."""
        sql = """
            UPDATE trips
            SET name = ?, location = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Trip instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM trips
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Trip object having the attribute values from the table row."""

        trip = cls.all.get(row[0])
        if trip:
            trip.name = row[1]
            trip.location = row[2]
        else:
            trip = cls(row[1], row[2])
            trip.id = row[0]
            cls.all[trip.id] = trip
        return trip

    @classmethod
    def get_all(cls):
        """Return a list containing a Trip object per row in the table"""
        sql = """
            SELECT *
            FROM trips
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Trip object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM trips
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Trip object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM trips
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None


class Activity:
    all = {}
    VALID_DAYS = ["Monday", "Tuesday", "Wednesday",
                  "Thursday", "Friday", "Saturday", "Sunday"]

    def __init__(self, activity_name, description, price, day, trip_id, id=None):
        self.day = day
        self.activity_name = activity_name
        self.description = description
        self.price = price
        self.id = id
        self.trip_id = trip_id

    @property
    def trip_id(self):
        return self._trip_id

    @trip_id.setter
    def trip_id(self, trip_id):
        if isinstance(trip_id, int):
            self._trip_id = trip_id
        else:
            raise Exception("trip_id must be an integer")

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day):
        if day in self.VALID_DAYS:
            self._day = day
        else:
            raise Exception("Day must be a valid day of the week.")

    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, activity_name):
        if isinstance(activity_name, str) and len(activity_name) in range(1, 25):
            self._activity_name = activity_name
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

    @classmethod
    def create_table(cls):
        sql = """ CREATE TABLE IF NOT EXISTS activities (
            id INTEGER PRIMARY KEY AUTOINCREMENT, activity TEXT NOT NULL, 
            description TEXT NOT NULL, price REAL NOT NULL, 
            day TEXT NOT NULL, trip_id INTEGER NOT NULL)"""
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """ DROP TABLE IF EXISTS activities;"""
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """ INSERT INTO activities (activity, description, price, day, trip_id)
        VALUES (?,?,?,?,?)"""

        CURSOR.execute(sql, (self.activity_name, self.description,
                       self.price, self.day, self.trip_id))
        CONN.commit()

    @classmethod
    def create(cls, activity_name, description, price, day, trip_id):
        activity = cls(activity_name, description, price, day, trip_id)
        activity.save()
        return activity

    def update(self):
        """Update the table row corresponding to the current Activity instance."""
        sql = """UPDATE activities SET activity = ?, description = ?, price = ?, day =? WHERE id = ?"""
        CURSOR.execute(sql, (self.activity_name, self.description,
                       self.price, self.day, self.id, self.trip_id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Activity instance."""

        sql = """DELETE FROM activities WHERE id = ?"""

        CURSOR.execute(sql, (self.id))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Activity object having the attribute values from table row."""

        activity = cls.all.get(row[0])
        if activity:
            activity.activity_name = row[1]
            activity.description = row[2]
            activity.price = row[3]
            activity.day = row[4]
            activity.trip_id = row[5]

        else:
            activity = cls(row[1], row[2], row[3], row[4], row[5])
            activity.id = row[0]
            activity.trip_id = row[5]
            cls.all[activity.id] = activity

    @classmethod
    def get_all(cls):
        """Return a list containing an Activity object per row in table."""
        sql = """SELECT * FROM activities"""
        rows = CURSOR.execute(sql).fetchall()

        activities = []
        for row in rows:
            activity = cls.instance_from_db(row)
            if activity:
                activities.append(activity)
        return activities

    @classmethod
    def find_by_id(cls, id):
        """Return an Activity object corresponding to the table row matching the specified primary key"""

        sql = """SELECT * FROM activities WHERE id = ?"""

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_activity_name(cls, activity_name):
        """Return an Activity object corresponding to first table row matching the specified name"""

        sql = """SELECT * FROM activities WHERE activity_name = ?"""

        row = CURSOR.execute(sql, (activity_name,)).fetchone()
        return cls.instance_from_db(row) if row else None
