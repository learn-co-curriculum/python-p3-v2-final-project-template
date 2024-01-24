import sqlite3 #database

from models.__init__ import CONN, CURSOR

CONN = sqlite3.connect("lib/gym.db") #connection
CURSOR = CONN.cursor() #pointer for the connection, row by row

class Exercise:

    # constructor
    def __init__(self, name, id=None):
        self.id = id # unknown now
        self.name = name
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 0 < len(value):
            self._name = value
        else:
            raise Exception("exercise must be of type string and longer than 0 characters.")

    def display_info(self):
        print(f"Exercise Name: {self.name}")

    @classmethod #affects the whole table, not just one row
    def create_table(cls): #this class as a parameter
        query = """
            CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY,
            name TEXT);
        """
        CURSOR.execute(query) #CURSOR takes the 'query' and executes it
        CONN.commit() #save the changes
    
    @classmethod
    def drop_table(cls):
        query = """
            DROP TABLE exercises;
        """
        CURSOR.execute(query)
        CONN.commit()

    #instance method / not class method
    def save(self):
        query = """
            INSERT INTO exercises (name)
            VALUES (?);
        """
        CURSOR.execute(query, (self.name,))
        CONN.commit() #save the changes
        self.id = CURSOR.lastrowid #update the id
        return self.id #return the id
    
    @classmethod
    def create(cls, name):
        exercise = Exercise(name)
        return exercise.save() #return the id
    
    @classmethod
    def new_form_db(cls, row):
        exercise = cls(
            name = row[1], #row at index 1 is the name
            id = row[0] #row at index 0 is the id
        )
        print(exercise.name, exercise.id)
        return exercise
    
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
    
    @classmethod
    def find_by_name(cls, first_name, last_name):
        sql = """
            SELECT * FROM trainer
            WHERE first_name = ? AND last_name = ?
            LIMIT 1;
        """
        CURSOR.execute(sql, (first_name, last_name))
        row = CURSOR.fetchone()
        if row:
            return cls.new_form_db(row)  # Assuming new_form_db constructs a Trainer instance
        else:
            return None




# Exercises
spin_class = Exercise("Spin Class")
boxing = Exercise("Boxing")
zumba = Exercise("Zumba")
step_class = Exercise("Step Class")
