
from models.__init__ import CONN, CURSOR

class Locale:
    all = []

    def __init__(self, location):
        self.location = location
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
    # if a member has locale that matches 1 2 or 3 add to members list
    
    def arcade(self):
        return [arcade for arcade in Arcade.all if arcade.location == self]
             
    def members(self):
        if list({arcade.member for arcade in self.arcade()}) == []:
            return "There are no members at this location"
        else:
            return list({arcade.member for arcade in self.arcade()})
    
    def __repr__(self):
        return f' Location name = "{self.location}" '
