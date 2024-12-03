import sqlite3
#how you connect to db?
CONN = sqlite3.connect('airline.db')
#how you connect WITH the db?
CURSOR = CONN.cursor()
