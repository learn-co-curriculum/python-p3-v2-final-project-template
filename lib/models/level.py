from models.__init__ import CONN, CURSOR

class Level:

    all_levels = {}

    def __init__(self, name, difficulty, string):
        self.name = name
        self.difficulty = difficulty
        self.string = string

    def __repr__(self) -> str:
        return f"<Level {self.name} {self.difficulty}>"

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Level instances """
        sql = """
            CREATE TABLE levels (
                id INTEGER PRIMARY KEY,
                name TEXT,
                difficulty TEXT,
                string TEXT
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Level instances """
        sql = """
            DROP TABLE IF EXISTS levels;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the values of the current Level instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO levels (name, difficulty, string)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.difficulty, self.string))
        CONN.commit()

        # Assign the id of the instance to be the table's last row id:
        self.id = CURSOR.lastrowid

        # Saves the instance to the "all_levels" dictionary:
        type(self).all_levels[self.id] = self

    @classmethod
    def create(cls, name, difficulty, string):
        """ Initialize a new Level instance and save the object to the database """
        level = cls(name, difficulty, string)
        level.save()
        return level
    
    def update(self):
        """Update the table row corresponding to the current Level instance."""
        sql = """
            UPDATE levels
            SET name = ?, difficulty = ?, string = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.difficulty, self.string, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Level instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM levels
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all_levels[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Level object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        level = cls.all_levels.get(row[0])
        if level:
            # ensure attributes match row values in case local instance was modified
            level.name = row[1]
            level.difficulty = row[2]
            level.string = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            level = cls(row[1], row[2], row[3])
            level.id = row[0]
            cls.all_levels[level.id] = level
        return level

    @classmethod
    def get_all(cls):
        """Return a list containing a Level object per row in the table"""
        sql = """
            SELECT *
            FROM levels
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Level object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM levels
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Level object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM levels
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None