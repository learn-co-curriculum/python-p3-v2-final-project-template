import sqlite3

CONN = sqlite3.connect('jeopardy.db')
CURSOR = CONN.cursor()
