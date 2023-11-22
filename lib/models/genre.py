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
        existing_id = CURSOR.fetchone()

        if existing_id:
            print(f'A genre with the name "{name}" already exists.')
        else:
            CURSOR.execute("INSERT INTO genres (name, description) VALUES (?, ?)", (name, description))
            CONN.commit()

     # delete by id
    def delete_by_id(self, genre_id):
        CURSOR.execute("SELECT name FROM genres WHERE id = ?", (genre_id))
        existing_name = CURSOR.fetchone()

        if existing_name:
            print(f"Deleting {existing_name} (id: {genre_id})...")
            CURSOR.execute("DELETE FROM genres WHERE id = ?", (genre_id)) 
            CONN.commit()
        else:
            print(f'A genre with the name "{existing_name}" does not exist.')
    
    # delete by name
    def delete_by_name(self, name):
        name_search = name.lower()
        CURSOR.execute("SELECT id FROM genres WHERE name = ?", (name_search))
        existing_id = CURSOR.fetchone()

        if existing_id:
            print(f"Deleting {name} (id: {existing_id})...")
            CURSOR.execute("DELETE FROM genres WHERE id = ?", (existing_id)) 
            CONN.commit()
        else:
            print(f'A genre with the name "{name}" does not exist.')
    
     # find genre by id
    def find_by_id(self, genre_id):
        CURSOR.execute("SELECT * FROM genres WHERE id = ?", (genre_id))
        existing_genre = CURSOR.fetchone()

        if existing_genre:
            return CURSOR.fetchone()
        else: 
            print(f'A genre with the id "{genre_id}" does not exist.')

    # find genre by name
    def find_by_name(self, name):
        name_search = name.lower()
        CURSOR.execute("SELECT * FROM genres WHERE name = ?", (name_search))
        existing_genre = CURSOR.fetchone()

        if existing_genre:
            return CURSOR.fetchone()
        else: 
            print(f'A genre with the name "{name}" does not exist.')

    # get all genres
    def get_all_genres(self):
        CURSOR.execute("SELECT * FROM genres")
        return CURSOR.fetchall()
