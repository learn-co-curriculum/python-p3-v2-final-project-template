class Band:
    def __init__(self, name, members, gender, home_city):
        self.name = name   
        self.members = members
        self.gender = gender
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
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        if isinstance(gender, str) and gender in ['male', 'female', 'mixed', 'other']:
            self._gender = gender
        else:
            raise Exception("Gender must be 'male', 'female', 'mixed', or 'other'")  

    @property
    def home_city(self):
        return self._home_city

    @home_city.setter
    def home_city(self, home_city):
        if isinstance(home_city, str) and len(home_city) > 0 and not hasattr(self, 'hometown'):
            self._home_city = home_city
        else:
            raise Exception("Home city must be a non-empty string") 
        
# This code must be in concert.py
        #concert band 
        #must be of type band
        #should be able ti change after the cocert is instantiated


    @property 
    def band(self):
        return self._band
    
    @band.setter
    def band(self, band):
        #from band import Band
        if isinstance(band, Band):
           self._band + band 
        else :
            raise Exception("Band must be an instrance of Band class!")
   

    def home_city_show(self):
        return f"The band {self.band.name} is playing a show in their home city, {self.band.home_city}, at {self.venue} on {self.date}."
    



# City band 
    
    #Return a unique list of all the bands for the city
   # Bands must be of type Band 
    

    def bands(self):
         return list(set([concert.band for concert in self.concert()]))