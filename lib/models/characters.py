from __init__ import CURSOR, CONN

class Character:


    def __init__(self, name, char_class, race, strengh, dexterity, constitution, intelligence, wisdom, charisma, alignment, player, active, id = None):
        self.name = name
        self.char_class = char_class
        self.race = race
        self.strengh = strengh
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.align = alignment
        self.player = player
        self.active = active
        self.id = id

    def __repr__(self):
        return f"<Chracter {self.id}: {self.name}, {self.char_class}, {self.race}, {self. strengh}, {self.dexterity}, {self.constitution}, {self.intelligence}, {self.wisdom}, {self.charisma}, {self.alignment}, {self.player}, {self.active}>"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str:
            if len(name) >= 5:
                self._name = name
            else: raise ValueError('!!Name must be at least 5 characters!!')
        else: raise ValueError('!!Name must be a string!!')

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
    def alignment(self):
        return self._alignment
    
    @alignment.setter
    def alignment(self, alignment):
        self._alignment = alignment

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

# UPDATES if id is already in the database -- SAVES a new character to the database ans assigns id
    def save(self):
        if self.id:
            sql = """
                UPDATE characters SET name =?, char_class = ?, race = ?, strengh = ?, dexterity = ?, constitution = ?, intelligence = ?, wisdom = ?, charisma = ?, alignment = ?, player = ?, active = ? WHERE id = ?
        """
            char_tuple = (self.name, self.char_class, self.race, self.strengh, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma, self.alignment, self.player, self.active)
            CURSOR.execute(sql, char_tuple)
            CONN.commit()
        else:
            sql = """
                INSERT INTO characters (name, char_class, race, strengh, dexterity, constitution, intelligence, wisdom, charisma, alignment, player, active) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
            char_tuple = (self.name, self.char_class, self.race, self.strengh, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma, self.alignment, self.player, self.active)
            CURSOR.execute(sql, char_tuple)
            CONN.commit()
            id_sql = """
                SELECT LAST_INSERT_ROWID() FROM characters
            """
            new_id_tuple = CURSOR.execute(id_sql).fetchone()
            self.id = new_id_tuple[0]

#creates a new character and saves it to the database
    @classmethod
    def create_char(cls, name, char_class, race, strengh, dexterity, constitution, intelligence, wisdom, charisma, alignment, player, active):
        character = Character(name, char_class, race, strengh, dexterity, constitution, intelligence, wisdom, charisma, alignment, player, active)
        character.save()
        return character
        

#deletes a character from the database and gets rid of id
    def delete_char(self):
        sql = """
            DELETE FROM characters WHERE id = ?;
        """
        char_tuple = (self.id,)
        CURSOR.execute(sql, char_tuple)
        CONN.commit()
        self.id = None

    def char_class(self):
        sql = """
            SELECT * FROM characters WHERE class = ?
    """
        char_class_tuple = (self.id,)
        list_of_char_class_tuple = CURSOR.execute(sql, char_class_tuple).fetchall()
        return [Character.dnd_data(row) for row in list_of_char_class_tuple]
    
    def race(self):
        sql = """
            SELECT * FROM characters WHERE race = ?
    """
        race_tuple = (self.id,)
        list_of_race_tuple = CURSOR.execute(sql, race_tuple).fetchall()
        return [Character.dnd_data(row) for row in list_of_race_tuple]

#given a row from the database---return with new instance with info from database
    @classmethod
    def dnd_data(cls, row_tuple):
        character = Character(row_tuple[1])
        character.id = row_tuple[0]
        return character

#returns a Character from dnd_data and gives instances of all Characters from the database
    @classmethod
    def all(cls):
        sql = """
            SELECT * FROM characters
        """
        char_list = CURSOR.execute(sql).fetchall()
        return [Character.dnd_data(row) for row in char_list]
    
    
# view related objects, and find an object by attribute
#char_class, race, strengh, dexterity, constitution, intelligence, wisdom, charisma, alignment, player, active