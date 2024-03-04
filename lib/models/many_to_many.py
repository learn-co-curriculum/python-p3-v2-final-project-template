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
    
    def __repr__(self):
        return f' Location name = "{self.location}" '
    
    def arcade(self):
        return [arcade for arcade in Arcade.all if arcade.location == self]
             
    def members(self):
        return list({arcade.members for arcade in self.arcade()})
    

class Member:
    all = []

    def __init__(self, member):
        self.member = member
        Member.all.append(self)

    @property
    def member(self):
        return self.member
    
    @member.setter
    def member(self, new_member):
        if not hasattr(self, "_member"):
            self._member = new_member

    def __repr__(self):
        return f' Member name = "{self.member}" '
    
    def locale(self):
        return [location for location in Arcade.all if location.member == self]
    
    def arcade(self):
        return [arcade for arcade in Arcade.all if arcade.member == self]


class Arcade:
    all = []

    def __init__(self, member, location):
        #this will pull the name from member
        self.member = member
        #based on membership level the person has access to 1, 2, or 3 locations
        self._location = location 
        #this will pull the membership 
        # self.tag = tag
        Arcade.add_access(self)

    @classmethod
    def add_access(cls, new_access):
        cls.all.append(new_access)

    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, new_location):
        if new_location is Locale:
            self._location = new_location
        else:
            raise ValueError("Please input a valid location")
    
    
    @classmethod
    def locations(cls):
        return [locale.location for locale in Locale.all]
    
    @classmethod
    def members(cls):
        return [members.member for members in Member.all]
    
    def __repr__(self):
        return f' Member name = "{self.members}" Location = "{self.locations}"'

    
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
        