# lib/models/team.py
from models.__init__ import CURSOR, CONN


class Team:

    def __init__(self, name, division, id=None):
        self.id = id
        self.name = name
        self.division = division

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
    def division(self):
        return self._division

    @division.setter
    def division(self, division):
        if isinstance(division, str) and len(division):
            self._division = division
        else:
            raise ValueError(
                "Division must be a non-empty string"
            )

    @classmethod
    def create_table(cls):
        sql = """
                CREATE TABLE IF NOT EXISTS teams (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                division TEXT
                ) """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Team instances """
        sql = """
            DROP TABLE IF EXISTS teams;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and division values of the current Team instance."""
        sql = """
            INSERT INTO teams (name, division)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.division))
        CONN.commit()

    # @classmethod
    # def create(cls, name, division):
    #     """ Initialize a new Team instance and save the object to the database """
    #     team = cls(name, division)
    #     team.save()
    #     return team

    # def update(self):
    #     """Update the table row corresponding to the current Team instance."""
    #     sql = """
    #         UPDATE teams
    #         SET name = ?, location = ?
    #         WHERE id = ?
    #     """
    #     CURSOR.execute(sql, (self.name, self.division, self.id))
    #     CONN.commit()

    # def delete(self):
    #     """Delete the table row corresponding to the current Team instance,
    #     delete the dictionary entry, and reassign id attribute"""

    #     sql = """
    #         DELETE FROM teams
    #         WHERE id = ?
    #     """

    #     CURSOR.execute(sql, (self.id,))
    #     CONN.commit()

    #     # Delete the dictionary entry using id as the key
    #     del type(self).all[self.id]

    #     # Set the id to None
    #     self.id = None

    # @classmethod
    # def instance_from_db(cls, row):
    #     """Return a Team object having the attribute values from the table row."""
    #     one_team = Team(row[1], row[2])
    #     one_team.id = row[0]
    #     return one_team

    @classmethod
    def get_all(cls):
        """Return a list containing a Team object per row in the table"""
        sql = """
            SELECT *
            FROM teams
        """
        rows = CURSOR.execute(sql).fetchall()
        return rows

    # @classmethod
    # def find_by_id(cls, id):
    #     """Return a Team object corresponding to the table row matching the specified primary key"""
    #     sql = """
    #         SELECT *
    #         FROM teams
    #         WHERE id = ?
    #     """

    #     row = CURSOR.execute(sql, (id,)).fetchone()
    #     return cls.instance_from_db(row) if row else None

    # @classmethod
    # def find_by_name(cls, name):
    #     """Return a Team object corresponding to first table row matching specified name"""
    #     sql = """
    #         SELECT *
    #         FROM teams
    #         WHERE name is ?
    #     """

    #     row = CURSOR.execute(sql, (name,)).fetchone()
    #     return cls.instance_from_db(row) if row else None

    # def employees(self):
    #     """Return list of employees associated with current team"""
    #     from models.employee import Employee
    #     sql = """
    #         SELECT * FROM employees
    #         WHERE team_id = ?
    #     """
    #     CURSOR.execute(sql, (self.id,),)

    #     rows = CURSOR.fetchall()
    #     return [
    #         Employee.instance_from_db(row) for row in rows
    #     ]
