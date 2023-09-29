
# scenario.py
import sqlite3

class Scenario:
    def __init__(self, name, description, monster_id):
        self.name = name
        self.description = description
        self.monster_id = monster_id

    @classmethod
    def initialize_scenario(cls, conn):
        cursor = conn.cursor()
        sql = """
            CREATE TABLE IF NOT EXISTS scenarios (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT NOT NULL
            )
        """
        cursor.execute(sql)
        conn.commit()

    def save(self, cursor, conn):
        sql = """
            INSERT INTO scenarios (name, description)
            VALUES (?, ?)
        """
        cursor.execute(sql, (self.name, self.description))
        conn.commit()

    @classmethod
    def get_random_scenarios(cls, cursor, num_scenarios):
        sql = """
            SELECT * FROM scenarios
            ORDER BY RANDOM()
            LIMIT ?
        """
        rows = cursor.execute(sql, (num_scenarios,)).fetchall()
        return [cls(row[1], row[2], row[0]) for row in rows]
