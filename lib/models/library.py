from models.__init__ import CONN, CURSOR

class Library:
    all = {}

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def _repr_(self):
        return f"<Library {self.id}: Name='{self.name}', Location='{self.location}'>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        if isinstance(location, str) and len(location):
            self._location = location
        else:
            raise ValueError("Location must be a non-empty string")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS libraries (
                id INTEGER PRIMARY KEY,
                name TEXT,
                location TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS libraries"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = "INSERT INTO libraries (name, location) VALUES (?, ?)"
        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = "UPDATE libraries SET name = ?, location = ? WHERE id = ?"
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM libraries WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name, location, *, librarian_name=None):
        library = cls(name, location)
        library.save()
        return library

    @classmethod
    def instance_from_db(cls, row):
        library = cls.all.get(row[0])
        if library:
            library.name = row[1]
            library.location = row[2]
        else:
            library = cls(row[1], row[2], row[0])
            cls.all[library.id] = library
        return library

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM libraries"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM libraries WHERE name = ?"
        rows = CURSOR.execute(sql, (name,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_location(cls, location):
        sql = "SELECT * FROM libraries WHERE location = ?"
        rows = CURSOR.execute(sql, (location,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]