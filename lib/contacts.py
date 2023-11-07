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
    
    @classmethod 
    def all(cls):
        sql = 'SELECT * FROM contacts'
        list_of_tuples = cursor.execute(sql).fetchall()
        return [Contact.from_db ( row ) for row in list_of_tuples]
    
    @classmethod
    def from_db( cls, row_tuple ):
        contact_instance = Contact( row_tuple[1], row_tuple[2])
        contact_instance.id = row_tuple[0]
        return contact_instance
    
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

    def save(self, cursor):
        if self.id is None:
            sql = "INSERT INTO contacts (first_name, last_name) VALUES (?, ?)"
            cursor.execute(sql, (self.first_name, self.last_name))
            self.id = cursor.lastrowid    
                
    def read_all():
        pass
    
    def update(self):
        pass
    
    def delete(self):
        pass