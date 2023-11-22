import sqlite3

CONN = sqlite3.connect('dnd_data.sqlite')
CURSOR = CONN.cursor()
