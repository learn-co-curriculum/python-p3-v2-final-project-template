# liv/models/team.py
from models.__init__ import CURSOR, CONN
from models.brand import Brand

class Driver:
    all = {}

    def __init__(self, name, brand_num, id=None):
        self.id = id
        self.name = name
        self.brand_num = brand_num

    def __repr__(self):
        return (
            f"<Driver {self.id}: {self.name}," +
            f"Car #: {self.brand_num}>"
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @property
    def brand_num(self):
        return self._brand_num

    @brand_num.setter
    def brand_num(self, brand_num):
        if type(brand_num) is int and Brand.find_by_id(brand_num):
            self._brand_num = brand_num
        else:
            raise ValueError(
                "brand_num must reference a brand # in the database")
    


    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS drivers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            brand_num INTEGER,
            FOREIGN KEY (brand_num) REFERENCES brands(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS drivers;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO drivers (name, brand_num) 
            VALUES (?,?)
        """


        CURSOR.execute(sql, (self.name, self.brand_num))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, brand_num):
        driver = cls(name, brand_num)
        driver.save()
        return driver

    def delete(self):
        sql = """
            DELETE FROM drivers
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        driver = cls.all.get(row[0])
        if driver:
            driver.name = row[1]
            driver.brand_num = row[2]
        else:
            driver = cls(row[1], row[2])
            driver.id = row[0]
            cls.all[driver.id] = driver
        return driver

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM drivers
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM drivers
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
