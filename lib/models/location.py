from models.__init__ import CURSOR, CONN

class Location:

    all = {}

    def __init__(self, city, id = None):
        self.id = id
        self.city = city
    
    def __repr__(self):
        return f"<Location {self.id}: {self.city}>"

    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, value):
        if isinstance(value, str) and 0 < len(value):
            self._city = value
        else:
            raise Exception("city must be of type string and greater than 0 characters long.")

    @classmethod
    def create_table(cls):
        query = """
            CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY,
            city TEXT);
        """
        CURSOR.execute(query)
        CONN.commit()

    @classmethod 
    def drop_table(cls):
        query = """
            DROP TABLE IF EXISTS locations;
        """
        CURSOR.execute(query)
        CONN.commit()

    def save(self):
        query = """
            INSERT INTO locations (city)
            VALUES (?);
        """
        CURSOR.execute(query, (self.city,))
        CONN.commit()

        self.id = CURSOR.lastrowid 
        type(self).all[self.id] = self

    @classmethod 
    def create(cls, city):
        location = cls(city)
        location.save()

        return location
    
    def update(self):
        sql = """
            UPDATE locations
            SET city = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.city, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM locations
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None
    
    @classmethod 
    def instance_from_db(cls, row):
        location = cls.all.get(row[0])

        if location:
            location.city = row[1]
        
        else:
            location = cls(row[1])
            location.id = row[0]
            cls.all[location.id] = location
        
        return location
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM locations
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        return cls.instance_from_db(row) if row else None
    
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

    def save(self):
        query = """
            INSERT INTO locations (city)
            VALUES (?);
        """
        CURSOR.execute(query, (self.city,))
        CONN.commit()
        self.id = CURSOR.lastrowid


