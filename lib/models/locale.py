
from models.__init__ import CONN, CURSOR

class Locale:
    all = []

    def __init__(self, location, id=None):
        self.location = location
        self.id = id 
        Locale.add_new_location(self)

    @classmethod
    def add_new_location(cls, new_instance):
        cls.all.append(new_instance)
        
    @property
    def location(self):
        return self._location

    @location.setter 
    def location(self, new_location):
         if not hasattr(self, "_location"):
             self._location = new_location
    
    #keep track of all the members that have access to a location
    
    
    def arcade(self):
        return [arcade for arcade in Arcade.all if arcade.location == self]
             
    def members(self):
        if list({arcade.member for arcade in self.arcade()}) == []:
            return "There are no members at this location"
        else:
            return list({arcade.member for arcade in self.arcade()})
    
    def __repr__(self):
        return f' <Location id = "{self.id}" name={self.name} '

    def save(self):
        sql = """
            INSERT INTO locations (location)
            VALUES (? )
            """
        CURSOR.execute(sql, (self.name, ))
        CONN.commit()

        self.id = CURSOR.lastrowid