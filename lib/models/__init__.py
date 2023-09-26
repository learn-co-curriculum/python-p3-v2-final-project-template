import sqlite3

CONN = sqlite3.connect('vacations.db')
CURSOR = CONN.cursor()
