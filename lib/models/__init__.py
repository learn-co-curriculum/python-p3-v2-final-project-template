import sqlite3

CONN = sqlite3.connect('dnd_data.db')
CURSOR = CONN.cursor()
