from models.__init__ import (CONN, CURSOR)
from models.player import Player
from models.level import Level

class Game:

    all_games = {}

    def __init__(self, player_id, level_id, player_input, time, accuracy):
        self.player_id = player_id
        self.level_id = level_id
        self.player_input = player_input
        self.time = time
        self.accuracy = accuracy

    def __repr__(self) -> str:
        return f"<Game Level: {self.level_id}>"

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Game instances """
        sql = """
            CREATE TABLE games (
                id INTEGER PRIMARY KEY,
                player_id INTEGER REFERENCES players(id),
                level_id INTEGER REFERENCES levels(id),
                player_input TEXT,
                time TEXT,
                accuracy REAL
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Game instances """
        sql = """
            DROP TABLE IF EXISTS games;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the values of the current Level instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO games (player_id, level_id, player_input, time, accuracy)
            VALUES (?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.player_id, self.level_id, self.player_input, self.time, self.accuracy))
        CONN.commit()

        # Assign the id of the instance to be the table's last row id:
        self.id = CURSOR.lastrowid

        # Saves the instance to the "all_levels" dictionary:
        type(self).all_games[self.id] = self

    @classmethod
    def create(cls, player_id, level_id, player_input, time, accuracy):
        """ Initialize a new Game instance and save the object to the database """
        game = cls(player_id, level_id, player_input, time, accuracy)
        game.save()
        return game
    
    def update(self):
        """Update the table row corresponding to the current Level instance."""
        sql = """
            UPDATE games
            SET player_id = ?, level_id = ?, player_input = ?, time = ?, accuracy = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.player_id, self.level_id, self.player_input, self.time, self.accuracy))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Game instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM game
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all_games[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Game object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        game = cls.all_games.get(row[0])
        if game:
            # ensure attributes match row values in case local instance was modified
            game.player_id = row[1]
            game.level_id = row[2]
            game.player_input = row[3]
            game.time = row[4]
            game.accuracy = row[5]
        else:
            # not in dictionary, create new instance and add to dictionary
            game = cls(row[1], row[2], row[3], row[4], row[5])
            game.id = row[0]
            cls.all_games[game.id] = game
        return game

    @classmethod
    def get_all(cls):
        """Return a list containing a Game object per row in the table"""
        sql = """
            SELECT *
            FROM games
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Game object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM games
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    