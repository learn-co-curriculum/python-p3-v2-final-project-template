from models.__init__ import CONN, CURSOR
from models.world import World
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
        return f'\n<Player id: {self.id}\n name: {self.name}\n  strength: {self.strength}\n  hp: {self.hp}>\n.'
    
    @classmethod
    def find_by_id(cls,id):
        sql = '''
            SELECT * FROM players WHERE id = ?
            '''
        row = CURSOR.execute(sql,(id,)).fetchone()
        return cls.from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = '''
            SELECT * FROM players WHERE name = ? 
        '''
        row = CURSOR.execute(sql,(name,)).fetchone()
        return cls.from_db(row) if row else None 
    
    @classmethod
    def create(cls,name):
        player = cls(name)
        player.save()
        return player
        
    def login(self, world):
        sql = 'INSERT INTO login (world_id, player_id) VALUES(?,?)'
        params_tuple = (world.id, self.id)
        CURSOR.execute(sql,params_tuple)
        CONN.commit()
    def worlds(self):
        sql = '''
            SELECT DISTINCT worlds.* FROM WORLDS
            JOIN login ON login.world_id = worlds.id
            WHERE login.player_id = ?
        '''
        params_tuple = (self.id,)
        list_of_tuples = CURSOR.execute(sql,params_tuple).fetchall()
        return [World.from_db(row) for row in list_of_tuples]
    
    #CREATE TABLE login(id INTEGER PRIMARY KEY,player_id INTEGER,world_id INTEGER);
    @classmethod 
    def create_table2(cls):
        sql = 'CREATE TABLE login(id INTEGER PRIMARY KEY,player_id INTEGER,world_id INTEGER)'
        CURSOR.execute(sql)

    @classmethod
    def all_player_login(cls):
        sql = '''
            SELECT * FROM login WHERE player_id = ? 
        '''
        list_of_tuples = CURSOR.execute(sql).fetchone()
        return [Player.login_db(row) for row in list_of_tuples]
    @classmethod
    def login_db(cls,row_tuple):
        player_instance = ( row_tuple[1],)
        player_instance.id = row_tuple[0]
        return player_instance
    # must create a table(will throw seed at project later)
    # need a player instace, and a world instance to login.
# ipdb> player1 = Player("Test7")
# ipdb> world1 = World("test4")
# ipdb> player1.save()
# ipdb> world1.save()
# ipdb> player1.login_history(world1)
# *** AttributeError: 'Player' object has no attribute 'login_history'
# ipdb> player1.login(world1)
# ipdb> player1.worlds()
# [
# <World id: 4 name: test4>
# .]