import sqlite3
from models.__init__ import CONN, CURSOR

class Book:
    all = {}
    allowed_genres = {"Fiction", "Non-Fiction", "Comics", "Fantasy", "Humor", "Romance"}

    def __init__(self, title, author, genre, year, price, id=None):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.price = price

    def __repr__(self):
        return f"<Book {self.id}: Title='{self.title}', Author='{self.author}', Genre='{self.genre}', Year={self.year}, Price={self.price}>"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError("Title must be a non-empty string")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, str) and len(author):
            self._author = author
        else:
            raise ValueError("Author must be a non-empty string")

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        if genre in self.allowed_genres:
            self._genre = genre
        else:
            raise ValueError(f"Genre must be one of {', '.join(self.allowed_genres)}")

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if isinstance(year, int) and year > 0:
            self._year = year
        else:
            raise ValueError("Year must be a positive integer")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, float) and price >= 0:
            self._price = price
        else:
            raise ValueError("Price must be a non-negative float")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                genre TEXT,
                year INTEGER,
                price REAL
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS books"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = "INSERT INTO books (title, author, genre, year, price) VALUES (?, ?, ?, ?, ?)"
        CURSOR.execute(sql, (self.title, self.author, self.genre, self.year, self.price))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = "UPDATE books SET title = ?, author = ?, genre = ?, year = ?, price = ? WHERE id = ?"
        CURSOR.execute(sql, (self.title, self.author, self.genre, self.year, self.price, self.id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM books WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, title, author, genre, year, price):
        book = cls(title, author, genre, year, price)
        book.save()
        return book

    @classmethod
    def instance_from_db(cls, row):
        book = cls.all.get(row[0])
        if book:
            book.title = row[1]
            book.author = row[2]
            book.genre = row[3]
            book.year = row[4]
            book.price = row[5]
        else:
            book = cls(row[1], row[2], row[3], row[4], row[5])
            book.id = row[0]
            cls.all[book.id] = book
        return book

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM books"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_genre(cls, genre):
        if genre not in cls.allowed_genres:
            raise ValueError(f"Genre must be one of {', '.join(cls.allowed_genres)}")
        sql = "SELECT * FROM books WHERE genre = ?"
        rows = CURSOR.execute(sql, (genre,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
