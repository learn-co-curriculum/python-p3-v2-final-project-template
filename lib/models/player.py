from models.__init__ import CONN, CURSOR
class Player:
    def __init__(self, name, strength = 1, hp = 10, id=None ):
        self.name = name 
        self.strength = strength
        self.hp = hp
        self.id = id
    
    @property 
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if not hasattr(self, "_name"):
            if isinstance(new_name, str) and 1 <= len(new_name) <= 10:
                self._name = new_name


    @classmethod 
    def create_table(cls):
        sql= '''
            CREATE TABLE players(
                id INTEGER PRIMARY KEY,
                name TEXT,
                strength INTEGER,
                HP INTEGER

            )
        '''
        CURSOR.execute(sql)
    
    def save(self):
        if self.id:
            sql: f'UPDATE players SET name = ?, strength = ?, hp = ?  WHERE id = ?'
            param_tuples = (self.name, self.strength, self.hp, self.id)
            CURSOR.execute(sql, param_tuples)
            CONN.commit()
        else:
            sql = 'INSERT INTO players (name,strength,hp) VALUES (?, ?, ? )'
            param_tuples = (self.name, self.strength, self.hp )
            CURSOR.execute(sql, param_tuples)
            CONN.commit()
            id_sql = 'SELECT LAST_INSERT_ROWID() FROM players'
            new_id_tuple = CURSOR.execute( id_sql ).fetchone()
            self.id = new_id_tuple[0]

    #Deletes player from db
    def deletes( self ):
        sql = 'DELETE FROM players WHERE id = ?'
        params_tuple = ( self.id, )
        CURSOR.execute( sql, params_tuple )
        CONN.commit()
        self.id = None
# V makes database display , work to create a instance with
    @classmethod
    def all(cls):
        sql = 'SELECT * FROM players'
        list_of_tuples = CURSOR.execute( sql ).fetchall()
        return [Player.from_db(row) for row in list_of_tuples]
    @classmethod
    def from_db(cls,row_tuple):
        player_instance = Player( row_tuple[1],row_tuple[2],row_tuple[3])
        player_instance.id = row_tuple[0]
        return player_instance
    def __repr__(self):
        return f'\n<Player id: {self.id} name: {self.name}>\n.'
    @classmethod
    def find_by_id(cls,id):
        sql = '''
            SELECT * FROM players WHERE id = ?
            '''
        row = CURSOR.execute(sql,(id,)).fetchone()
        return cls.from_db(row) if row else None
        
    
    




  

