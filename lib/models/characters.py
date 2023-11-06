from __init__ import CURSOR, CONN

class Character:


    def __init__(self, name, char_class, race, strengh, dexterity, constitution, intelligence, wisdom, charisma, align, player, active, id = None):
        self.name = name
        self.char_class = char_class
        self.race = race
        self.strengh = strengh
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.align = align
        self.player = player
        self.active = active

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 3:
            self._name = name

    @property
    def char_class(self):
        return self._char_class
    
    @char_class.setter
    def char_class(self, char_class):
        

    @property
    def race(self):
        return self._race
    
    @race.setter
    def name(self, race):
        

#create an object, delete an object, display all objects, view related objects, and find an object by attribute.

#    @classmethod
#    def all(cls):
#        sql = 'SELECT * FROM characters'
#        query_object = CURSOR.execute(sql)
#        char_list = query_object.fetchall()
#        return char_list
#    
