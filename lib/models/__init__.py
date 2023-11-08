import sqlite3

CONN = sqlite3.connect('cars.db')
CURSOR = CONN.cursor()
