import sqlite3

CONN = sqlite3.connect('lib/gym.db')
CURSOR = CONN.cursor()
