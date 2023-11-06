from models.__init__ import CONN, CURSOR

class Genre: 
    def __init__(self):
        self.create_table()

    # create genre table
    def create_table(self):
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS genres (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT
            )
        ''')
        CONN.commit()
    
    # add genre
    def add_genre(self, name, description):
        name_new = name.lower()
        CURSOR.execute("SELECT id FROM genres WHERE name = ?", (name_new))
        existing_new = CURSOR.fetchone()

        if existing_new:
            print(f'A genre with the name "{name}" already exists.')
        else:
            CURSOR.execute("INSERT INTO genres (name, description) VALUES (?, ?)", (name, description))
            CONN.commit()
