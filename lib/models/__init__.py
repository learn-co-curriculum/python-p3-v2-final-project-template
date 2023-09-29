import sqlite3

CONN = sqlite3.connect('game.db')
CURSOR = CONN.cursor()

# CURSOR.execute("DROP TABLE IF EXISTS scenarios")
# CONN.commit()
# uncomment and use this as a template to drop tables, run this file &
# re-run any of the models to update db as needed.
def close_connection():
    CONN.close()
