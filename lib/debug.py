#!/usr/bin/env python3
# lib/debug.py

from datetime import datetime
from models.book import Book
from models.author import Author
from models.borrowinghistory import BorrowingHistory
from models.library import Library
from models.category import Category
from models.user import User
import ipdb

def reset_database():
    Book.drop_table()
    Book.create_table()

    Author.drop_table()
    Author.create_table()

    Category.drop_table()
    Category.create_table()

    User.drop_table()
    User.create_table()

    BorrowingHistory.drop_table()
    BorrowingHistory.create_table()

    Library.drop_table()
    Library.create_table()

    # Create seed data for authors
    fitzgerald = Author.create("F. Scott Fitzgerald")
    lee = Author.create("Harper Lee")
    orwell = Author.create("George Orwell")
    austen = Author.create("Jane Austen")

    # Create seed data for categories
    fiction = Category.create("Fiction")
    comics = Category.create("Comics")
    fantasy = Category.create("Fantasy")
    humor = Category.create("Humor")
    romance = Category.create("Romance")

    # Create seed data for books
    Book.create("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1925, 19.25)


    # Create seed data for users
    User.create("Alice", "alice@example.com", "password123")
    User.create("Bob", "bob@example.com", "password123")
    User.create("Charlie", "charlie@example.com", "password123")

    # Create seed data for borrowing history
    BorrowingHistory.create(1, 1, datetime.now(), None)

    # Create seed data for library
    Library.create("Main Library", "123 Library St", librarian_name="Librarian Name")

reset_database()
ipdb.set_trace()