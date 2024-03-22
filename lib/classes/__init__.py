import sqlite3

CONN = sqlite3.connect('ticket_triage.db')
CURSOR = CONN.cursor()
