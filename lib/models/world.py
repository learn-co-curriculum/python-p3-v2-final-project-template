from models.__init__ import CONN, CURSOR
class World:
    def __init__(self, location,id=None):
        self.location = location
        self.id = id
    
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self,new_location):
        if not hasattr(self, '_location'):
            if type(new_location) == str and 1 <= len(new_location) <= 15:
                self._location = new_location
    
    @classmethod 
    def create_table(cls):
        sql= '''
            CREATE TABLE worlds(
                id INTEGER PRIMARY KEY,
                location TEXT
            )
        '''
        CURSOR.execute(sql)

    def save(self):
        if self.id:
            sql: f'UPDATE worlds SET location = ? WHERE id = ?'
            param_tuples = (self.location, self.id)
            CURSOR.execute(sql, param_tuples)
            CONN.commit()
        else:
            sql = 'INSERT INTO worlds (location) VALUES (?)'
            param_tuples = (self.location, )
            CURSOR.execute(sql, param_tuples)
            CONN.commit()
            id_sql = 'SELECT LAST_INSERT_ROWID() FROM worlds'
            new_id_tuple = CURSOR.execute( id_sql ).fetchone()
            self.id = new_id_tuple[0]
# Deletes World from db
    def shatter( self ):
        sql = 'DELETE FROM worlds WHERE id = ?'
        params_tuple = ( self.id, )
        CURSOR.execute( sql, params_tuple )
        CONN.commit()
        self.id = None
# V makes database display , work to create a instance with
    @classmethod
    def all(cls):
        sql = 'SELECT * FROM worlds'
        list_of_tuples = CURSOR.execute( sql ).fetchall()
        return [World.from_db(row) for row in list_of_tuples]

    @classmethod
    def from_db(cls,row_tuple):
        world_instance = World( row_tuple[1])
        world_instance.id = row_tuple[0]
        return world_instance

    def __repr__(self):
        return f'\nWorld id: {self.id}\n name: {self.location}\n'
    

    @classmethod
    def find_by_id(cls, id):
        sql = '''
            SELECT * FROM worlds WHERE id = ?
        '''
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.from_db(row) if row else None

    @classmethod
    def create(cls,location):
        world = cls(location)
        world.save()
        return world
