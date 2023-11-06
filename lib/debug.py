#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import connection, cursor
import ipdb
class Contact: 
    
    def __init__ ( self, first_name, last_name, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

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
    
    def __repr__(self):
        return f'<Contact id: {self.id} first_name: {self.first_name} last_name: {self.last_name}>'


class Address: 
    def __init__ (self, email, id= None )
        self.email = email
        self.id = id

ipdb.set_trace()
