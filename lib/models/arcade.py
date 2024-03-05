class Arcade:
    all = []

    def __init__(self, member, tag, location):
        #this will pull the name from member
        self.member = member
        #based on membership level the person has access to 1, 2, or 3 locations
        self.location = location 
        #this will pull the membership 
        # self.tag = tag
        Arcade.add_access(self)
    
    @property
    def member(self):
        return self._member
    
    @member.setter
    def member(self, new_member):
        if not hasattr(self, "_member"):
            if type(new_member) == str:
                if 1<= len(new_member) <= 10:
                 self._member = new_member
                else:
                    raise ValueError("All new members must be betweeen 1 and 10 characters")
            else:
                raise TypeError("Name must be a string")
            
        raise AttributeError("Name is not able to be changed")
    
    @property
    def tag(self):
        self.tage = self.tag
    @tag.setter
    def tag(self, new_tag):
        if isinstance(self, new_tag):
            if 3 <= len(new_tag) <= 15:
                    self._tag = new_tag
            else:
                raise ValueError("This tag must be at least 3 and 15 characters long")
        else:
            raise TypeError("Name must be a string")

    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, new_location):
        if isinstance(new_location, Locale):
            self._location = new_location
        else:
            raise TypeError("Location must be a Locale class instance")
    
    @classmethod
    def locations(cls):
        return [locale.location for locale in Locale.all]
    
    @classmethod
    def members(cls):
        return [member.members for member in Member.all]
    
    @classmethod
    def add_access(cls, new_access):
        cls.all.append(new_access)


    def __repr__(self):
        return f'{self.member} // {self.location}'