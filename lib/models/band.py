class Band:
    def __init__(self, name, members, genre, home_city):
        self.name = name   
        self.members = members
        self.genre = genre
        self.home_city = home_city

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise Exception("Band name must be a non-empty string")  

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
    def genre(self):
        return self._genre

    @genre.setter
    
    def home_city(self):
        return self._home_city

    @home_city.setter
    def home_city(self, home_city):
        if isinstance(home_city, str) and len(home_city) > 0 and not hasattr(self, 'hometown'):
            self._home_city = home_city
        else:
            raise Exception("Home city must be a non-empty string") 
        

  

# City band 
    
    #Return a unique list of all the bands for the city
   # Bands must be of type Band 
    

    def bands(self):
         return list(set([concert.band for concert in self.concert()]))