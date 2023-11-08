#lib/models/brand.py
from models.__init__ import CURSOR, CONN


class Brand:

    all = {}

    def __init__(self, name, coo, id=None):
        self.id = id
        self.name = name
        self.coo = coo

    def __repr__(self):
        return f"<Brand #{self.id}: {self.name}, {self.coo}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Your car brand must be a string"
            )
    @property
    def coo(self):
        return self._coo

    @coo.setter
    def coo(self, coo):
        if isinstance(coo, str) and len(coo):
            self._coo = coo
        else:
            raise ValueError(
                "coo must be a non-empty string"
            )

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS brands (
            id INTEGER PRIMARY KEY,
            name TEXT,
            coo TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS brands;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO brands (name, coo) 
            VALUES (?,?)
        """

        CURSOR.execute(sql, (self.name, self.coo))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        
    @classmethod
    def create(cls, name, coo):
        brand = cls(name, coo)
        brand.save()
        return brand

    def delete(self):
        sql = """
            DELETE FROM brands
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        brand = cls.all.get(row[0])
        if brand:
            brand.name = row[1]
            brand.coo = row[2]
        else:
            brand = cls(row[1], row[2])
            brand.id = row[0]
            cls.all[brand.id] = brand
        return brand

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM brands
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]


    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM brands
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def delete(self):

        sql = """
            DELETE FROM brands
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM brands
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def drivers(self):
        from models.driver import Driver
        sql = """
            SELECT * FROM drivers
            WHERE brand_num = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Driver.instance_from_db(row) for row in rows
        ]
