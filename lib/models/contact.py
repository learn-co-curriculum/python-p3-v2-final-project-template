
# from address import Address
from models.__init__ import CURSOR, CONN

class Contact:
    def __init__ (self, name, id=None):
        self.name = name
        self.id = id
    # def __init__(self, name:str):
    #     self._id = -1
    #     self.name = name

    def __repr__( self ):
        return f'id: {self.id} name: {self.name}'
    
    # def __repr__(self):
    #     return f"Contact(id={self._id}, name={self.name})"

    @classmethod
    def get_id (cls, id):
        sql = 'SELECT * FROM contacts WHERE id = ?'
        CURSOR.execute(sql, (id,))
        result = CURSOR.fetchone()
        if result:
            return Contact.from_db(result)
        else:
            return None
        
    @classmethod
    def get_name (cls, name):
        sql = 'SELECT * FROM contacts where name= ?'
        CURSOR.execute(sql, (name,))
        result= CURSOR.fetchone()
        if result:
            return Contact.from_db(result)
        else:
            return None

    
    @classmethod 
    def all(cls):
        sql = 'SELECT * FROM contacts'
        list_of_tuples = CURSOR.execute(sql).fetchall()
        return [Contact.from_db ( row ) for row in list_of_tuples]
    
    @classmethod
    def from_db( cls, row_tuple ):
        contact_instance = Contact( row_tuple[1])
        contact_instance.id = row_tuple[0]
        return contact_instance
    

    # @property
    # def id(self):
    #     return self._id
        
    def __create_table__():
        sql = """CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER NOT NULL, 
            name VARCHAR(30) NOT NULL, 
            PRIMARY KEY (id)
        );
        """
        CURSOR.execute(sql)
        
    def create(name: str):
        sql = "INSERT INTO contacts (name) VALUES (?)"
        c = CURSOR.execute(sql, (name,))
        CONN.commit()
        return c.lastrowid

    # def save(self, CURSOR):
    #     if self.id is None:
    #         sql = "INSERT INTO contacts (first_name, last_name) VALUES (?, ?)"
    #         CURSOR.execute(sql, (self.first_name, self.last_name))
    #         self.id = CURSOR.lastrowid    
                
    # def read_all():
    #     sql = "select id, name from contacts"
    #     rows = CURSOR.execute(sql)
    #     ret = []
    #     for (id, name) in rows:
    #         person = Contact(name)
    #         person._id = id
    #         ret.append(person)
            
    #     return ret
    
    def show_detail(id:int):
        pass
        # sql = "SELECT name from contacts where id=?"
        # rows = CURSOR.execute(sql, (id,))
        # for (name) in rows:
        #     sql = "select "
        # selected = 
        
    def update(name:str, id:int):
        sql = "UPDATE contacts SET name=? WHERE id=?"
        if id < 0:
            print("cannot update with unsaved data. call create first")
            return
        
        c = CURSOR.execute(sql, (name, id))
        CONN.commit()
    
    def delete(id:int):
        sql = "DELETE FROM addresses WHERE person_id=?"
        CURSOR.execute(sql, (id,))
        sql = "DELETE FROM contacts WHERE id=?"
        CURSOR.execute(sql, (id,))
        CONN.commit()
        
    def addresses(self):
        from address import Address
        sql= """"
            SELECT * FROM addresses
            WHERE person_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Address.instance_from_db(row) for row in rows
        ]
if __name__ == "__main__":
    Contact.__create_table__()
    