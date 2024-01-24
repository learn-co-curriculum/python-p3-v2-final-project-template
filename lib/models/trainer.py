import sqlite3

CONN = sqlite3.connect("lib/gym.db") #connection
CURSOR = CONN.cursor() 

class Trainer:

    def __init__(self, first_name, last_name, id=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.create_table()
    
    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, value):
        if isinstance(value, str) and 0 < len(value):
            self._first_name = value
        else:
            raise Exception("first name needs to be of type string and greater than 0 characters long.")
    
    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self, value):
        if isinstance(value, str) and 0 < len(value):
            self._last_name = value
        else:
            raise Exception("last name needs to be of type string and greater than 0 characters long.")

    def create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS trainers (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT
            );
        """
        self.CURSOR.execute(query)
        self.CONN.commit()

    @classmethod #affects the whole table, not just one row
    def create_table(cls): #this class as a parameter
        query = """
            CREATE TABLE IF NOT EXISTS trainers (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT
            );
        """
        CURSOR.execute(query) #CURSOR takes the 'query' and executes it
        CONN.commit() #save the changes

    @classmethod
    def drop_table(cls):
        query = """
            DROP TABLE trainers;
        """
        CURSOR.execute(query)
        CONN.commit()

    #instance method / not class method
    def save(self):
        query = """
            INSERT INTO trainers (first_name, last_name)
            VALUES (?, ?);
        """
        CURSOR.execute(query, (self.first_name, self.last_name,))
        CONN.commit() #save the changes
        self.id = CURSOR.lastrowid #update the id
        # return self.id #return the id
    
    @classmethod
    def create(cls, name):
        trainer = Trainer(name)
        return trainer.save() #return the id
    
    @classmethod
    def new_form_db(cls, row):
        trainer = cls(
            name = row[1], #row at index 1 is the name
            id = row[0] #row at index 0 is the id
        )
        print(trainer.name, trainer.id)
        return trainer
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM trainers;
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        trainers = []
        for row in rows:
            trainer = cls.new_form_db(row)
            trainers.append(trainer)
        return trainers
    
    def display_info(self):
        print(f"Trainer Name: {self.first_name} {self.last_name}")





#trainer = Trainer("Kathy")

