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
        