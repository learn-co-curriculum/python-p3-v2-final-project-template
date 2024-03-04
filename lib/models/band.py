class Band:
    def __init__(self, name, members, genre , home_city):
        self.name = name   
        self.members = members
        self.genre  = genre 
        self.home_city = home_city
    
 

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise Exception("Band name must be a non-empty string")  # Changed ValueError to Exception

    @property
    def members(self):
        return self._members

    @members.setter
    def members(self, members):
        if isinstance(members, list) and len(members) > 0:
            self._members = members
        else:
            raise Exception("Members must be a non-empty list") 
    @property
    def genre (self):
        return self._genre 

    @genre .setter
    def genre (self, genre ):
        if isinstance(genre , str) and genre  in ['male', 'female', 'mixed', 'other']:
            self._genre  = genre 
        else:
            raise Exception("genre  must be 'male', 'female', 'mixed', or 'other'")  

    @property
    def home_city(self):
        return self._home_city

    @home_city.setter
    def home_city(self, home_city):
        if isinstance(home_city, str) and len(home_city) > 0 and not hasattr(self, 'hometown'):
            self._home_city = home_city
        else:
            raise Exception("Home city must be a non-empty string") 
        
#
   

    def home_city(self):
        return f"The band {self.band.name} is playing a show in their home city, {self.band.home_city}, at {self.venue} on {self.date}."
    

    def concert(self):
        from models.concert import Concert
        return [concert for concert in Concert.all if concert.band == self]
    

    def city(self):
        return list(set([concert.venue for concert in self.concerts()]))
