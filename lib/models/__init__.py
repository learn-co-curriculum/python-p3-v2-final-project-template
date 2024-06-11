import sqlite3

CONN = sqlite3.connect('library.db')
CURSOR = CONN.cursor()
