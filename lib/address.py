from typing import List
# from typing import Optional
from models.__init__ import CURSOR, CONN

class Address:
    latest = None
    def __init__(self, email:str, person_id:int):
        self._id = -1
        self.email = email
        self.person_id = person_id
        Address.latest = self

    def __repr__(self):
        return f"Address(id={self._id}, email={self.email}, person_id={self.person_id})"
    
    @property    
    def id(self):
        return self._id
        
    def __create_table__():
        sql = """create table addresses (
            id INTEGER NOT NULL, 
            email VARCHAR(30) NOT NULL, 
            person_id INTEGER NOT NULL, 
            PRIMARY KEY (id),
            FOREIGN KEY(person_id) REFERENCES contacts (id)
        );
        """
        CURSOR.execute(sql)

    def save(self, cursor, contact_id):
        if self.id is None:
            sql = "INSERT INTO addresses (contact_id, email) VALUES (?, ?)"
            cursor.execute(sql, (contact_id, self.email))
            self.id = cursor.lastrowid
        
    def create(self):
        pass
    
    def read_all():
        pass
    
    def update_email(self, new_email:str):
        pass
    
    def update_person_id(self, person_id:int):
        pass
    
    pass delete(self):
        pass