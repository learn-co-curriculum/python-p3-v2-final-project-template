import sqlite3

from models.__init__ import CONN, CURSOR

CONN = sqlite3.connect("lib/gym.db") #connection
CURSOR = CONN.cursor() 

class Trainer:
    CONN = sqlite3.connect("gym.db")
    CURSOR = CONN.cursor()

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.create_table()

    def create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS trainer (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT
            );
        """
        self.CURSOR.execute(query)
        self.CONN.commit()

    def display_info(self):
        print(f"Trainer Name: {self.first_name} {self.last_name}")

    @classmethod #affects the whole table, not just one row
    def create_table(cls): #this class as a parameter
        query = """
            CREATE TABLE IF NOT EXISTS exercise (
            id INTEGER PRIMARY KEY,
            name TEXT);
        """
        CURSOR.execute(query) #CURSOR takes the 'query' and executes it
        CONN.commit() #save the changes

    @classmethod
    def drop_table(cls):
        query = """
            DROP TABLE exercise;
        """
        CURSOR.execute(query)
        CONN.commit()

    #instance method / not class method
    def save(self):
        query = """
            INSERT INTO exercise (name)
            VALUES (?);
        """
        CURSOR.execute(query, (self.name,))
        CONN.commit() #save the changes
        self.id = CURSOR.lastrowid #update the id
        return self.id #return the id
    
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
            SELECT * FROM exercise;
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        exercises = []
        for row in rows:
            exercise = cls.new_form_db(row)
            exercises.append(exercise)
        return exercises





#trainer = Trainer("Kathy")

