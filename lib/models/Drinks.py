class Drinks():
    age_requirement = 21

    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("ID has to be an int")
        self._id = value
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name has to be a string")
        self._name = value
        