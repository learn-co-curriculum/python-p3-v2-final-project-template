class Arcade:
    all = []

    def __init__(self, member, location):
        #this will pull the name from member
        self.member = member
        #based on membership level the person has access to 1, 2, or 3 locations
        self.location = location 
        #this will pull the membership 
        # self.tag = tag
        Arcade.add_access(self)

    @classmethod
    def add_access(cls, new_access):
        cls.all.append(new_access)

    @property
    def member(self):
        return self._member
    
    @member.setter
    def member(self, new_member):
        if isinstance(new_member, Member):
            self._member = new_member
        else:
            raise ValueError("All new members must be an instance of Member Class")

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
    
    def __repr__(self):
        return f'{self.member} // {self.location}'
