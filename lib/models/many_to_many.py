class Local:
    def __init__(self, location):
        self.location = location

    @property
    def location(self):
        return self._location

    @location.setter 
    def location(self, new_location):
         if not hasattr(self, "_location"):
             self._location = new_location








class Player:
    def __init__(self, name, tag, membership):
        self.name = name
        self.tag = tag
        self.membership = membership

class Arcade:
    def __init__(self, name, location, member):
        self.name = name
        self.location = location 
        self.member = member
        

