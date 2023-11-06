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
