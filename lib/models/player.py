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


    




  

