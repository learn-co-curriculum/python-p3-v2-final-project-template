from __init__ import CURSOR, CONN
from utils import custom_property, SQL_drop_table

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

    @staticmethod
    def create_table():
        sql = """
            CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY,
            name STRING)
        """
        CURSOR.execute(sql)
        CONN.commit()

    # create_table = SQL_create_table("cities")

    drop_table = SQL_drop_table("cities")

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
    def instance_from_db(cls, row):
        city = cls.working_insts.get(row[0])
        if city:
            city.name = row[1]
        else:
            city = cls(row[1])
            city.id = row[0]
        return city

    @classmethod
    def find_by_id(cls, id):
        sql = """
        SELECT *
        FROM cities
        WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
        SELECT *
        FROM cities
        WHERE name = ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def update(self):
        sql = """
            UPDATE cities
            SET name = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM cities
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).working_insts[self.id]
        self.id = None

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM cities
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

# City.create_table()
# City.create('New York')
# c = City("Anchorage")

# City.drop_table()