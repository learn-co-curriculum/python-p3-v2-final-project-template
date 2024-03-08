from models.__init__ import CONN, CURSOR

class Locale:
    all = []

    def __init__(self, location, id=None):
        self.location = location
        self.id = id 
        Locale.add_new_location(self)

    @classmethod
    def add_new_location(cls, new_instance):
        cls.all.append(new_instance)

    @property
    def location(self):
        return self._location

    @location.setter 
    def location(self, new_location):
         if not hasattr(self, "_location"):
             self._location = new_location

    # Keep track of all the members that have access to a location
    def arcade(self):
        return [arcade for arcade in Arcade.all if arcade.location == self]

    def members(self):
        if list({arcade.member for arcade in self.arcade()}) == []:
            return "There are no members at this location"
        else:
            return list({arcade.member for arcade in self.arcade()})

    def __repr__(self):
        return f' <Location id = "{self.id}" name={self.location} '

    def save(self):
        sql = """
            INSERT INTO locations (location)
            VALUES (? )
            """
        CURSOR.execute(sql, (self.location, ))
        CONN.commit()

        self.id = CURSOR.lastrowid

    @classmethod
    def find_by_location(cls, location):
        sql = "SELECT * FROM locations WHERE location = ?"
        CURSOR.execute(sql, (location,))
        result = CURSOR.fetchone()
        if result:
            return Locale(result[1], result[0])
        return None

    @classmethod
    def create_table(cls):
        """create table if location if doesn't exist"""

        sql="""
            CREATE TABLE IF NOT EXISTS locations(
            id INTEGER PRIMARY KEY,
            location TEXT
            );
            """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM locations"
        CURSOR.execute(sql)
        results = CURSOR.fetchall()
        locations = [Locale(location, id) for id, location in results]
        return locations    