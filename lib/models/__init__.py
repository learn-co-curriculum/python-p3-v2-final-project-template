import sqlite3

CONN = sqlite3.connect('medical.db')
CURSOR = CONN.cursor()
