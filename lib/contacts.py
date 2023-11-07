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
        
    def read_all():
        pass
    
    def update(self):
        pass
    
    def delete(self):
        pass