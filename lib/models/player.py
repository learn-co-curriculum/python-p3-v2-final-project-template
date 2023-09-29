from models.__init__ import CURSOR, CONN
import re

class Player:
    ALL = {}

    def __init__(self, username, email, id=None, hit_points=150):
        self.id = id
        self._username = username
        self._email = email
        self.hit_points = hit_points
        self.max_hit_points = 150

    def __repr__(self):
        return f"{self.username} (HP: {self.hit_points})"

    # def __repr__(self):
    #     return (
    #         f"<Player {self.id}: {self.username}, "
    #         f"Email: {self.email}>"
    #     )

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username, is_username_unique):
        if not isinstance(username, str):
            raise ValueError("Username must be a string.")

        if not 3 <= len(username) <= 20:
            raise ValueError("Username must be between 3 and 20 characters.")

        if not re.match("^[a-zA-Z0-9_]*$", username):
            raise ValueError(
                "Username can only contain letters, numbers, and underscores."
                )

        if not is_username_unique(username):
            raise ValueError("This username is already taken. Sowie.")

        self._username = username

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email, is_email_unique):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Email is not in a valid format.")

        if not is_email_unique(email):
            raise ValueError("This email is already taken.")

        self._email = email

    @classmethod
    def create_table(cls):
        # SQL command to create new Player table to persist attribute's Player instance
        sql = """
            CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        # SQL command to drop Player table that persists Player instances
        sql = """
            DROP TABLE IF EXISTS players;
        """
        CURSOR.execute(sql)
        CONN.commit()

    # def save(self):
    #     # Save player instance to new database row
    #     sql = """
    #         INSERT INTO players (username, email)
    #         VALUES (?, ?)
    #     """

    #     # Update object id attribute using the primary key value of new row
    #     CURSOR.execute(sql, (self.username, self.email))
    #     CONN.commit()

    #     # Save the object in local dictionary using table row's PK as dictionary key
    #     self.id = CURSOR.lastrowid
        #     type(self).ALL[self.id] = self
    def save(self):
        data = (self.username, self.email)
        sql = """
            INSERT INTO players (username, email)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, data)
        CONN.commit()
        self.id = CURSOR.lastrowid


    def update(self):
        # Update this player's table row corresponding to the current Player instance
        sql = """
            UPDATE players
            SET username = ?, email = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.username, self.email, self.id))
        CONN.commit()

    def delete(self):
        # Delete this player from database
        sql = """
            DELETE FROM players
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).ALL[self.id]

        # Set id to None
        self.id = None

    @classmethod
    def create(cls, username, email):
        player = cls(username, email)
        player.save()
        return player


    @classmethod
    def instance_from_db(cls, row):
        # Return a Player object with attributes from correct table row

        # Check the dictionary for an existing instance using the row's primary key
        player = cls.ALL.get(row[0])
        if player:
            # ensure attributes match row values in case local instance was modified
            player.username = row[1]
            player.email = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            player = cls(row[1], row[2])
            player.id = row[0]
            cls.ALL[player.id] = player
        return player

    @classmethod
    def get_all(cls):
        # Return a list containing all player instances
        sql = """
            SELECT *
            FROM players
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        # Find a player by their ID
        sql = """
            SELECT *
            FROM players
            WHERE id = ?
        """
        # Return Player object from the table row with matching primary key
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_username(cls, username):
        # Find a player by their username
        sql = """
            SELECT *
            FROM players
            WHERE username is ?
        """
        # Return the first table row of a Player object matching a username
        row = CURSOR.execute(sql, (username,)).fetchone()
        return cls.instance_from_db(row) if row else None


    @classmethod
    def is_username_unique(cls, username):
        # Search in-memory
        is_unique_in_memory = not any(player.username == username for player in cls.ALL.values())

        # Search in database
        sql = """
            SELECT *
            FROM players
            WHERE username is ?
        """
        row = CURSOR.execute(sql, (username,)).fetchone()
        is_unique_in_db = row is None

        # if a result, return False; else: return True
        return is_unique_in_db and is_unique_in_memory

    @classmethod
    def is_email_unique(cls, email):
        # Search in-memory
        is_unique_in_memory = not any(player.email == email for player in cls.ALL.values())


        # Search in database
        sql = """
            SELECT *
            FROM players
            WHERE email is ?
        """
        row = CURSOR.execute(sql, (email,)).fetchone()
        is_unique_in_db = row is None

        # if a result, return False (not unique); else: return True
        return is_unique_in_db and is_unique_in_memory
