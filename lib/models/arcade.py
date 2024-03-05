
class Arcade:
    all = []

    def __init__(self, name, location,  tag=''):
        self.name = name
        self.location = location 
        self.tag = tag
        Arcade.add_access(self)

    @classmethod
    def add_access(cls, new_access):
        cls.all.append(new_access)

    @property
    def tag(self):
        return self._tag
    
    @tag.setter
    def tag(self, new_tag):
        self._tag = new_tag
        
    @property
    def tag(self):
        return self._tag
    
    @tag.setter
    def tag(self, new_tag):
        #add logic to make sure there are no duplicate tags
        if 5 <= len(new_tag) <= 15:
            self._tag = new_tag
        else:
            raise ValueError(f'Tag {new_tag} is not between 5 and 15 characters, please enter a different tag')