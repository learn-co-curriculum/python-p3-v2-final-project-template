from models import Book
from database import Session

def list_books():
    session = Session()
    books = session.query(Book).all()
    
    if not books:
        print("No books available.")
    else:
        print("Available books:")
        for book in books:
            print(book)
    session.close()

def add_book():
    print("Add a new book:")
    print("Please enter the book details.")
    title = input("Title: ")
    author = input("Author: ")
    genre = input("Genre: ")

    if not title or not author or not genre:
            print("All fields are required.")
            return

    session = Session()
    new_book = Book(title=title, author=author, genre=genre)
    session.add(new_book)
    session.commit()
    print("Book added.")
    session.close()

def borrow_book():
    list_books()
    book_id = int(input("Enter book ID to borrow: "))
    
    session = Session()
    book = session.query(Book).get(book_id)
    if book and not book.is_borrowed:
        book.is_borrowed = True
        session.commit()
        print(f"You borrowed '{book.title}'.")
    else:
        print("Book not available.")
    session.close()

def return_book():
    list_books()
    book_id = int(input("Enter book ID to return: "))
    
    session = Session()
    book = session.query(Book).get(book_id)
    if book and book.is_borrowed:
        book.is_borrowed = False
        session.commit()
        print(f"You returned '{book.title}'.")
    else:
        print("Book is not currently borrowed.")
    session.close()
