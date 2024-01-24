import sqlite3

from models.__init__ import CONN, CURSOR

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()
