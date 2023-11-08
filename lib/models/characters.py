import sqlite3
CONN = sqlite3.connect('dnd_data.sqlite')
CURSOR = CONN.cursor()

class Character:

    def __init__(self, name, char_class, race, strength, dexterity, constitution, intelligence, wisdom, charisma, alignment, player_id, level, active = 0, id = None):
        self.name = name
        self.char_class = char_class
        self.race = race
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.alignment = alignment
        self.player_id = player_id
        self.active = active
        self.id = id
        self.level = level

    def __repr__(self):
        return f"<{self.name}, the {self.char_class} {self.race}, Level {self.level}>"


# UPDATES if id is already in the database -- SAVES a new character to the database ans assigns id
    def save(self):
        if self.id:
            sql = """
                UPDATE characters SET 
                name =?, 
                class = ?, 
                race = ?, 
                strength = ?, 
                dexterity = ?, 
                constitution = ?, 
                intelligence = ?, 
                wisdom = ?, 
                charisma = ?, 
                alignment = ?, 
                player_id = ?, 
                active = ?, 
                level = ?, 
                WHERE id = ?
        """
            char_tuple = (self.name, 
                self.char_class, 
                self.race, 
                self.strength, 
                self.dexterity, 
                self.constitution, 
                self.intelligence, 
                self.wisdom, 
                self.charisma, 
                self.alignment, 
                self.player_id, 
                self.active,
                self.level,
                self.id
            )
            CURSOR.execute(sql, char_tuple)
            CONN.commit()
        else:
            sql = """
                INSERT INTO characters 
                (name, class, race, strength, dexterity, constitution, intelligence, wisdom, charisma, alignment, player_id, active, level) 
                VALUES 
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
            char_tuple = (self.name, self.char_class, self.race, self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma, self.alignment, self.player_id, self.active, self.level)
            CURSOR.execute(sql, char_tuple)
            CONN.commit()
            id_sql = """
                SELECT LAST_INSERT_ROWID() FROM characters
            """
            new_id_tuple = CURSOR.execute(id_sql).fetchone()
            self.id = new_id_tuple[0]

#creates a new character and saves it to the database
    @classmethod
    def create_char(cls, name, char_class, race, strength, dexterity, constitution, intelligence, wisdom, charisma, alignment, player_id, level):
        character = Character(name, char_class, race, strength, dexterity, constitution, intelligence, wisdom, charisma, alignment, player_id, level)
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

    # def get_active(self, )

#given a row from the database---return with new instance with info from database
    @classmethod
    def dnd_data(cls, row_tuple):
        character = Character(row_tuple[1], row_tuple[2], row_tuple[3],
            row_tuple[4], row_tuple[5], row_tuple[6], row_tuple[7], row_tuple[8], 
            row_tuple[9], row_tuple[10], row_tuple[12], row_tuple[13], 
            row_tuple[11], row_tuple[0])
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
#char_class, race, strength, dexterity, constitution, intelligence, wisdom, charisma, alignment, player_id, active

    @classmethod
    def my_chars(cls, current_player):
        sql = """
            SELECT * FROM characters WHERE player_id = ?;
        """
        var_tuple = (current_player.id,)
        char_list = CURSOR.execute(sql, var_tuple).fetchall()
        return [Character.dnd_data(row) for row in char_list]

    def update_active(self):
        sql = """
            UPDATE characters SET active = 0 WHERE player_id = ?;
        """
        var_tuple = (self.player_id,)
        CURSOR.execute(sql, var_tuple)
        CONN.commit()
        sql = """
            UPDATE characters SET active = 1 WHERE id = ?;
        """
        var_tuple = (self.id,)
        CURSOR.execute(sql, var_tuple)
        CONN.commit()
