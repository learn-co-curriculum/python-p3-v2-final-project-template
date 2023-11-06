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
    
 
