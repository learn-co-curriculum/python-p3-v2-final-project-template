import sqlite3

CONN = sqlite3.connect('address_book.db')
CURSOR = CONN.cursor()
