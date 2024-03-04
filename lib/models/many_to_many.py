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

    
class Arcade:
    all = []

    def __init__(self, name, location, membership, tag=''):
        #this will pull the name from member
        self.name = name
        #based on membership level the person has access to 1, 2, or 3 locations
        self.location = location 
        #this will pull the membership 
        self.membership = membership
        self.tag = tag
        Arcade.add_access(self)

    @classmethod
    def add_access(cls, new_access):
        cls.all.append(new_access)


    @property
    def membership(self):
        return self._membership
    
    @membership.setter
    def membership(self, new_membership):
        if new_membership == 1 or new_membership == 2 or new_membership ==3:
            self._membership = new_membership
        else:
            raise ValueError("Please input a valid membership level of 1, 2, or 3")
        
    @property
    def tag(self):
        return self._tag
    
    @tag.setter
    def tag(self, new_tag):
        #logic to make sure there are no duplicate tags
        if 5 <= len(new_tag) <= 15:
            self._tag = new_tag
        else:
            raise ValueError(f'Tag {new_tag} is not between 5 and 15 characters, please enter a different tag')
        