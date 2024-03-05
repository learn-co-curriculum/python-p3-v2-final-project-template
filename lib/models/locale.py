class Locale:

    def __init__(self, location):
        self.location = location
        
    @property
    def location(self):
        return self._location

    @location.setter 
    def location(self, new_location):
         if not hasattr(self, "_location"):
             self._location = new_location
    
    #keep track of all the members that have access to a location
    # if a member has locale that matches 1 2 or 3 add to members list
             
    def members(self):
        [member for member in Arcade.all if member.location == self ]
      

