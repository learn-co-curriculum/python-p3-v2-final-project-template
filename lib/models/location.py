import sqlite3 

from models.__init__ import CONN, CURSOR

CONN = sqlite3.connect('lib/gym.db')
CURSOR = CONN.cursor()


class Location:
    all = []
    def __init__(self, city, id = None):
        self._city = city
        self.id = id
        Location.all.append(self)

    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value):
        self._city = value

    @staticmethod 
    def display_all_locations():
        for location in Location.all:
            print(location.city)

    def display_info(self):
        print(f"Location: {self.name}")

    @classmethod
    def create_table(cls):
        query = """
            CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY,
            city TEXT);
        """
        CURSOR.execute(query)
        CONN.commit()

    # @classmethod 
    # def drop_table(cls):
    #     query = """
    #         DROP TABLE IF EXISTS `location_table`;
    #     """
    #     CURSOR.execute(query)
    #     CONN.commit()


    def save(self):
        query = """
            INSERT INTO locations (city)
            VALUES (?);
        """
        CURSOR.execute(query, (self.city,))
        CONN.commit()
        self.id = CURSOR.lastrowid 

    @classmethod 
    def create_location_row(cls, city):
        location = cls(city)
        location.save()
        return location
    
    @classmethod 
    def new_location_db(cls, row):
        location = cls (
                id = row[0],
                city = row[1]
            )
        return location 
    
    @classmethod 
    def get_all_locations(cls):
        sql = """
            SELECT * FROM locations
        """
        return [cls.new_location_db(one_row) for one_row in CURSOR.execute(sql).fetchall()]
    
    @classmethod 
    def find_by_name(cls, city):
        sql = """
            SELECT * FROM locations
            WHERE city = ? 
            LIMIT 1;
        """
        row = CURSOR.execute(sql, (city,)).fetchone()
        if not row:
            return None
        return Location(
            city = row[1],
            id = row[0]
        )

