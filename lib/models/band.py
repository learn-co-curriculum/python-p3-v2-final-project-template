from __init__ import CURSOR, CONN
from utils import custom_property, SQL_drop_table

class Band:

    working_insts = {}

    def __init__(self, name, members, genre, home_city):
        self.name = name   
        self.members = members
        self.genre = genre
        self.home_city = home_city

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise Exception("Band name must be a non-empty string")  

    @property
    def members(self):
        return self._members

    @members.setter
    def members(self, members):
        if isinstance(members, list) and len(members) > 0:
            self._members = members
        else:
            raise Exception("Members must be a non-empty list") 
    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        self._genre = genre
    
    @property
    def home_city(self):
        return self._home_city

    @home_city.setter
    def home_city(self, home_city):
        if isinstance(home_city, str) and len(home_city) > 0 and not hasattr(self, 'hometown'):
            self._home_city = home_city
        else:
            raise Exception("Home city must be a non-empty string") 
        

  

# City band 
    
    #Return a unique list of all the bands for the city
   # Bands must be of type Band 
    

    def bands(self):
         return list(set([concert.band for concert in self.concert()]))
    
    

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS bands (
            id INTEGER PRIMARY KEY,
            name TEXT,
            members TEXT,
            genre TEXT,
            home_city_id INTEGER,
            FOREIGN KEY (home_city_id) REFERENCES cities(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS bands
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        members_str = ','.join(self.members)
        sql = """
            INSERT INTO bands (name, members, genre, home_city_id)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, members_str, self.genre, self.home_city)) #will have to replace home city with an id
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).working_insts[self.id] = self

    @classmethod
    def create(cls, name, members, genre, home_city_id):
        band = cls(name, members, genre, home_city_id)
        band.save()
        return band

    @classmethod
    def instance_from_db(cls, row):
        band_id, name, members_str, genre, home_city_id = row
        members = members_str.split(',')
        band = cls.working_insts.get(band_id)
        if band:
            band.name = name
            band.members = members
            band.genre = genre
            band.home_city_id = home_city_id
        else:
            band = cls(name, members, genre, home_city_id)
            band.id = band_id
        return band

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM bands
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM bands
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None



# Band.create_table()
# Band.create('The Example', ['Member 1', 'Member 2'], 'Rock', 1) 