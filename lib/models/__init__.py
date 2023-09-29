import sqlite3

CONN = sqlite3.connect('game.db')
CURSOR = CONN.cursor()

CURSOR.execute("DROP TABLE IF EXISTS scenarios")
CONN.commit()
def close_connection():
    CONN.close()
