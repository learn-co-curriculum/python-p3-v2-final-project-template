from models.__init__ import CURSOR, CONN
from models.utils import custom_property, SQL_drop_table, SQL_get_all, SQL_show_all, SQL_find_by_attribute, SQL_delete

def name_conds(name):
    if not isinstance(name, str):
        raise TypeError("City name must be a string")
    if not name.strip():
        raise ValueError("City name cannot be blank")
    if not 2 <= len(name) <= 60:
        raise ValueError("City name length must be between 2 and 60 characters")
    return True

class City:

    working_insts = {}
    table_name = "cities"

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

        self.working_insts[self.id] = self

    def __repr__(self):
        return f'<City {self.id}: {self.name}>'

    def __str__(self): 
        return f'    {self.name} (id: {self.id})'

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

    drop_table = SQL_drop_table(table_name)

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

    def delete(self):
        #delete key from concerts
        sql = """
            UPDATE concerts
            SET city_id = NULL
            WHERE city_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        #delete key from bands
        sql = """
            UPDATE bands
            SET home_city_id = NULL
            WHERE home_city_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        #delete entry from cities and cleanup id
        SQL_delete(type(self).table_name)(self)

    get_all = SQL_get_all()
    show_all = SQL_show_all()
    find_by_id = SQL_find_by_attribute("id")
    find_by_name = SQL_find_by_attribute("name")