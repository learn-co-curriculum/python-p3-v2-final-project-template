import sqlite3
CONN = sqlite3.connect('database.db')

CURSOR = CONN.cursor()

class Categories:
    all = {}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name
    
@classmethod
def create_table(cls):
    try:
        CURSOR.execute(f'''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            );
        ''')
    except Exception as e:
        return e

@classmethod
def drop_table(cls):
    try:
        CURSOR.execute(f'''
            DROP TABLE IF EXISTS
''')
    except Exception as e:
        return e
    
@classmethod
def new(cls,name):
    new_category = cls(name)
    new_category.save()
    return new_category

def save(self):
    with CONN:
        cursor = CONN.cursor()
        if self.id is None:
            cursor.execute('INSERT INTO categories (name) VALUES (?)', (self.name))
            self.id = cursor.lastrowid
        else:
            cursor.execute('UPDATE categories SET name = ? WHERE id = ?', (self.name, self.id))