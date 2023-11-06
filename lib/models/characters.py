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
        self.id = id

    def __repr__(self):
        return f"<Chracter {self.id}: {self.name}, {self.char_class}, {self.race}, {self. strengh}, {self.dexterity}, {self.constitution}, {self.intelligence}, {self.wisdom}, {self.charisma}, {self.align}, {self.player}, {self.active}>"

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
        self._char_class = char_class

    @property
    def race(self):
        return self._race
    
    @race.setter
    def race(self, race):
        self._race = race
    
    @property
    def strengh(self):
        return self._strengh
    
    @strengh.setter
    def strengh(self, strengh):
        self._strengh = strengh

    @property
    def dexterity(self):
        return self._dexterity
    
    @dexterity.setter
    def dexterity(self, dexterity):
        self._dexterity = dexterity

    @property
    def constitution(self):
        return self._constitution
    
    @constitution.setter
    def constitution(self, constitution):
        self._constitution = constitution

    @property
    def intelligence(self):
        return self._intelligence
    
    @intelligence.setter
    def intelligence(self, intelligence):
        self._intelligence = intelligence

    @property
    def wisdom(self):
        return self._wisdom
    
    @wisdom.setter
    def wisdom(self, wisdom):
        self._wisdom = wisdom

    @property
    def charisma(self):
        return self._charisma
    
    @charisma.setter
    def charisma(self, charisma):
        self._charisma = charisma

     @property
    def align(self):
        return self._align
    
    @align.setter
    def align(self, align):
        self._align = align

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        self._player = player

     @property
    def active(self):
        return self._active
    
    @active.setter
    def active(self, active):
        self._active = active

    @classmethod
    def create_char(cls):
        """ Create a new table to persist the attributes of Department instances """
        sql = """
            CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

        def delete_char(self):
            sql = """
                DEL FROM characters WHERE id = ?;
        """


    @classmethod
    def all(cls):
        sql = """
            SELECT * FROM characters
        """
        char_list = CURSOR.execute(sql).fetchall()
        return char_list
    
#create an object, delete an object, view related objects, and find an object by attribute.