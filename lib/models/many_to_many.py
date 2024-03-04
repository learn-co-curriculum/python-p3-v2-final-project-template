class Local:
    def __init__(self, location):
        self.location = location

    @property
    def location(self):
        return self._location

    @location.setter 
    def location(self, new_location):
         if not hasattr(self, "_location"):
             self._location = new_location

class Member:
    all = []

    def __init__(self, member, tag, membership):
        self.member =  member
        self.tag = tag
        self.membership = membership
        Member.add_new_member(self)

    @classmethod
    def add_new_member(cls, new_instance):
        cls.all.append(new_instance)

    @property
    def member(self):
        return self._member
    
    @member.setter
    def member(self, new_member):
        if not hasattr(self, "_member"):
            self._member = new_member

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
        
    @property
    def membership(self):
        return self._membership
    
    @membership.setter
    def membership(self, new_membership):
        #make sure memberhsip level is 1,2, or 3
        if new_membership == 1 or new_membership == 2 or new_membership == 3:
            self._membership = new_membership
        else:
            raise ValueError("Please input a valid membership level of 1, 2, or 3")


        

class Arcade:
    def __init__(self, member, location, ):
        self.member = member
        self.location = location 
        

    @property
    def member(self,):
        return self._member
    
    @name.setter
    def name(self, new_member):
        return []
   
   
   
   
   
    # @property
    # def location(self):
    #     return self._location

    # @location.setter 
    # def location(self, new_location):
    #      if not hasattr(self, "_location"):
    #          self._location = new_location

    

