import sqlite3

CONN = sqlite3.connect('game.db')
CURSOR = CONN.cursor()
