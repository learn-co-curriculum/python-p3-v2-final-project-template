class Locale:
    all = []

    def __init__(self, location):
        self.location = location
        Locale.all.append(self)

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
    

class Member:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not hasattr(self, "_name"):
            self._name = new_name
    
    def arcade(self):
        return [arcade for arcade in Arcade.all if arcade.member == self]

    def locations(self):
        return list({arcade.location for arcade in self.arcade()})
    
    def __repr__(self):
        return f' Member name = "{self.name}" '
    


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

    
    # @property
    # def tag(self):
    #     return self._tag
    
    # @tag.setter
    # def tag(self, new_tag):
    #     #logic to make sure there are no duplicate tags
    #     if 5 <= len(new_tag) <= 15:
    #         self._tag = new_tag
    #     else:
    #         raise ValueError(f'Tag {new_tag} is not between 5 and 15 characters, please enter a different tag')
        