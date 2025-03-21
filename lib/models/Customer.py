class Customer():
    def __init__(self, name, age):
        #self.id = id
        self.name = name
        self.age = age
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("ID has to be an Int")
        self._id = value
    
    @property
    def name(self):
        return self._name

    @id.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name has to be a string")
        if 1 <= len(value) >= 10: 
            raise ValueError("Name has to be from 1-10 characters")
        self._name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age has to be of type int")
        if 1 <= value >= 122:
            raise ValueError("Enter a valid age")
        self._age = value