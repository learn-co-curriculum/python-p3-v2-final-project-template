from models.__init__ import CONN, CURSOR
import ipdb


class Drinks():
    age_requirement = 21

    def __init__(self, name, id=None):
        self._id = id
        self.name = name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name has to be a string")
        self._name = value

    def save(self):
        sql = """
            INSERT INTO drinks (name)
            VALUES (?);
        """
        
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
    
        self._id = CURSOR.lastrowid

    def update(self):
        sql = """
            UPDATE drinks
            SET name = ?,
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM drinks
            WHERE id = ?;
        """

        CURSOR.execute(sql, (self._id,))
        CONN.commit()
        self._id = None

    @classmethod
    def instance_from_row(cls, row):
        return cls(name=row[1], id=row[0])

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM drinks;
        """

        drinks_rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_row(row) for row in drinks_rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM drinks
            WHERE id = ?;
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        if row:
            return cls.instance_from_row(row)
        else:
            return None

    @classmethod
    def create(cls, name):
        new_drink = cls(name=name)
        new_drink.save()
        return new_drink

    @classmethod
    def delete_all(cls):
        sql = """
            DELETE FROM drinks;
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS drinks (
               id INTEGER PRIMARY KEY,
               name TEXT
            );
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS drinks;"

        CURSOR.execute(sql)
        CONN.commit()

    def __repr__(self):
        return f'<drinks id={self._id} name={self.name} >'
        