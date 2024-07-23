import sqlite3

CONN = sqlite3.connect('lib/db/kitz.db')
CURSOR = CONN.cursor()
