from typing import List
from typing import Optional
from models.address import Address
from models.__init__ import CURSOR, CONN

class Contact:
    latest = None
    def __init__(self, name:str):
        self._id = -1
        self.name = name
        Contact.latest = self
    
    def __repr__(self):
        return f"Contact(id={self._id}, name={self.name})"
    
    # @classmethod 
    # def all(cls):
    #     sql = 'SELECT * FROM contacts'
    #     list_of_tuples = CURSOR.execute(sql).fetchall()
    #     return [Contact.from_db ( row ) for row in list_of_tuples]
    
    # @classmethod
    # def from_db( cls, row_tuple ):
    #     contact_instance = Contact( row_tuple[1], row_tuple[2])
    #     contact_instance.id = row_tuple[0]
    #     return contact_instance
    
    @property
    def id(self):
        return self._id
        
    def __create_table__():
        sql = """create table contacts (
            id INTEGER NOT NULL, 
            name VARCHAR(30) NOT NULL, 
            PRIMARY KEY (id)
        );
        """
        CURSOR.execute(sql)
        
    def create(self):
        sql = "INSERT INTO contacts (name) VALUES (?)"
        c = CURSOR.execute(sql, (self.name,))
        CONN.commit()
        self._id = c.lastrowid
        return c.lastrowid

    # def save(self, CURSOR):
    #     if self.id is None:
    #         sql = "INSERT INTO contacts (first_name, last_name) VALUES (?, ?)"
    #         CURSOR.execute(sql, (self.first_name, self.last_name))
    #         self.id = CURSOR.lastrowid    
                
    def read_all():
        sql = "select id, name from contacts"
        rows = CURSOR.execute(sql)
        ret = []
        for (id, name) in rows:
            person = Contact(name)
            person._id = id
            ret.append(person)
            
        return ret
    
    def update(self):
        sql = "UPDATE contacts SET name=? WHERE id=?"
        if self._id < 0:
            print("cannot update with unsaved data. call create first")
            return
        
        c = CURSOR.execute(sql, (self.name,self._id))
        CONN.commit()
    
    def delete(self, id=-1):
        if id < 0:
            id = self._id
        sql = "DELETE from contacts WHERE id=?"
        if id < 0:
            print("cannot update with unsaved data. call create first")
            return
        
        c = CURSOR.execute(sql, (self._id,))
        CONN.commit()
        
if __name__ == "__main__":
    Contact.__create_table__()
    