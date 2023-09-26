from models.__init__ import CURSOR, CONN
import re

class Player:
    all = {}

    def __init__(self, username, email, id=None, hit_points=150):
        self.id = id
        self.username = username
        self.email = email
        self.hit_points = hit_points
        self.max_hit_points = 150

    def __repr__(self):
        return f"{self.username} (HP: {self.hit_points})"

    def __repr__(self):
        return (
            f"<Player {self.id}: {self.username}, "
            f"Email: {self.email}>"
        )

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
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
    def email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Email is not in a valid format.")

        if not is_email_unique(email):
            raise ValueError("This email is already taken.")

        self._email = email

    @classmethod
    def create_table(cls):
        # SQL command to create Player table
        pass

    @classmethod
    def drop_table(cls):
        # SQL command to drop Player table
        pass

    def save(self):
        # Save player instance to database
        pass

    def update(self):
        # Update this player's data
        pass

    def delete(self):
        # Delete this player from database
        pass

    @classmethod
    def create(cls, username):
        # Create and return a new player instance
        pass

    @classmethod
    def instance_from_db(cls, row):
        # Initialize an instance from a database row
        pass

    @classmethod
    def get_all(cls):
        # Get all player instances
        pass

    @classmethod
    def find_by_id(cls, id):
        # Find a player by their ID
        pass

    @classmethod
    def find_by_username(cls, username):
        # Find a player by their username
        pass


    @classmethod
    def is_username_unique(cls, username):
        # Search in db or in-memory
        # if a result, return False
        # else: return True
        pass

    @classmethod
    def is_email_unique(cls, email):
        # Search in db or in-memory
        # if a result, return False
        # else: return True
        pass
