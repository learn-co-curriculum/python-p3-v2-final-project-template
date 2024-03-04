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
        return [member for member in Arcade.all if member.location == self ]
    

class Member:
    all = []

    def __init__(self, name):
        self.name = name
        Member.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not hasattr(self, "_name"):
            self._name = new_name

    def __repr__(self):
        return f' Member name = "{self.name}" '
    
    def locale(self):
        return [location for location in Arcade.all if location.name == self]
    
    def arcade(self):
        return [arcade for arcade in Arcade.all if arcade.name == self]

class Arcade:
    all = []

    def __init__(self, name, location, membership):
        #this will pull the name from member
        self.name = name
        #based on membership level the person has access to 1, 2, or 3 locations
        self.location = location 
        #this will pull the membership 
        self.membership = membership
        # self.tag = tag
        Arcade.add_access(self)

    @classmethod
    def add_access(cls, new_access):
        cls.all.append(new_access)

    @property
    def membership(self):
        return self._membership
    
    @membership.setter
    def membership(self, new_membership):
        if new_membership == 1 or new_membership == 2 or new_membership == 3:
            self._membership = new_membership
        else:
            raise ValueError("Please input a valid membership level of 1, 2, or 3")
    
    def __repr__(self):
        return f' Member name = "{self.name}" Location = "{self.location}" Memership level = "{self.membership}" '
    
    @classmethod
    def locations(cls):
        return [locale.location for locale in Locale.all]
    
    @classmethod
    def members(cls):
        return [members.name for members in Member.all]

    
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
        