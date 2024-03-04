from __init__ import CURSOR, CONN
from utils import custom_property, SQLDropTable

def name_conds(name):
    if not isinstance(name, str):
        raise TypeError("City name must be a string")
    if not name.strip():
        raise ValueError("City name cannot be blank")
    if not 2 <= len(name) <= 25:
        raise ValueError("City name length must be between 2 and 25 characters")
    return True

class City:

    working_insts = {}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<City {self.id}: {self.name}>'

    name = custom_property(name_conds)

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY,
            name STRING)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
            sql = """
                DROP TABLE IF EXISTS cities
                """

        CURSOR.execute(sql)
        CONN.commit()

    drop_table = classmethod(SQLDropTable("cities"))

    def save(self):
        sql = """
            INSERT INTO cities (name)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).working_insts[self.id] = self

    @classmethod
    def create(cls, name):
        city = cls(name)
        city.save()
        return city

    @classmethod
    # i don't like this method ill probably use something different
    def instance_from_db(cls, row):
        city = cls.working_insts.get(row[0])
        if city:
            city.name = row[1]
        else:
            city = cls(row[1])
            city.id = row[0]
        return city

City.create_table()
City.create('New York')