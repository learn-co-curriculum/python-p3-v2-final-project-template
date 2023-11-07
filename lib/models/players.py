# lib/models/team.py
from models.__init__ import CURSOR, CONN
from models.team import Team

class Players:

    def __init__(self, name, team):
        self.name = name
        self.team = team

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if type(new_name) == str and len(new_name) > 0:
            self._name = new_name
        else:
            raise ValueError("Player name must be a string at least 1 character long")
    name = property(get_name, set_name)


    def get_team(self):
        return self._team
    def set_team(self, new_team):
        if isinstance(new_team, Team):
                self._team = new_team
    team = property(get_team, set_team)


    @classmethod
    def create_table(cls):
        sql = """ 
            CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            name TEXT,
            team INTEGER,
            FOREIGN KEY (team) REFERENCES teams(id)
        )"""
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS players"""
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO players (name, team)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.team.id))
        CONN.commit()
        return self

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM players
        """
        rows = CURSOR.execute(sql).fetchall()
        return rows