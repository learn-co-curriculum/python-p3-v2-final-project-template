import sqlite3

CONN = sqlite3.connect('game.db')
CURSOR = CONN.cursor()

# Try to add the has_healing_item column if it doesn't exist
try:
    CURSOR.execute('''
        ALTER TABLE monsters
        ADD COLUMN has_healing_item BOOLEAN NOT NULL DEFAULT FALSE
    ''')
    CONN.commit()
except sqlite3.OperationalError as e:
    # Catch the specific error if the column already exists
    if "duplicate column name" not in str(e):
        raise  # Re-raise the exception if it's a different error

# Now, it's safe to insert your monsters
monsters = [
    ("Wolf", 75, True),
    ("Orc", 125, False),
    ("Spooky Skeleton", 85, True),
    ("Silver wolf", 65, False),
    ("Drunken man", 90, True),
    ("Cunning witch", 85, True),
    ("Large spider", 100, False),
]

CURSOR.executemany('INSERT INTO monsters (name, hit_points, has_healing_item) VALUES (?, ?, ?)', monsters)
CONN.commit()

CONN.close()
