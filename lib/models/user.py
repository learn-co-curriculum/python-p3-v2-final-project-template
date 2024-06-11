import sqlite3
from models.__init__ import CONN, CURSOR

class User:
    all = {}

    def __init__(self, username, email, password, id=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User {self.id}: Username='{self.username}', Email='{self.email}'>"

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username):
            self._username = username
        else:
            raise ValueError("Username must be a non-empty string")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if isinstance(email, str) and len(email):
            self._email = email
        else:
            raise ValueError("Email must be a non-empty string")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        if isinstance(password, str) and len(password):
            self._password = password
        else:
            raise ValueError("Password must be a non-empty string")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                email TEXT,
                password TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS users"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = "INSERT INTO users (username, email, password) VALUES (?, ?, ?)"
        CURSOR.execute(sql, (self.username, self.email, self.password))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = "UPDATE users SET username = ?, email = ?, password = ? WHERE id = ?"
        CURSOR.execute(sql, (self.username, self.email, self.password, self.id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM users WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, username, email, password):
        user = cls(username, email, password)
        user.save()
        return user

    @classmethod
    def instance_from_db(cls, row):
        user = cls.all.get(row[0])
        if user:
            user.username = row[1]
            user.email = row[2]
            user.password = row[3]
        else:
            user = cls(row[1], row[2], row[3], row[0])
            cls.all[user.id] = user
        return user

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM users"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_username(cls, username):
        sql = "SELECT * FROM users WHERE username = ?"
        rows = CURSOR.execute(sql, (username,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_email(cls, email):
        sql = "SELECT * FROM users WHERE email = ?"
        rows = CURSOR.execute(sql, (email,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
