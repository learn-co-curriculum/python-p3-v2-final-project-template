from models.__init__ import CURSOR, CONN

class Exercise:

    all = []

    # constructor
    def __init__(self, name, id=None):
        self.id = id # unknown now
        self.name = name
        Exercise.all.append(self)
    
    def __repr__(self):
        return f"<Exercise {self.id}: {self.name}>"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise Exception("exercise must be of type string and longer than 0 characters.")

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
            SELECT * FROM exercises;
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        exercises = []
        for row in rows:
            exercise = cls.new_form_db(row)
            exercises.append(exercise)
        return exercises

    
    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM exercises WHERE name = ? LIMIT 1;"
        CURSOR.execute(sql, (name,))
        row = CURSOR.fetchone()
        if row:
            return cls.new_from_db(row)
        else:
            return None

    @classmethod
    def new_from_db(cls, row):
        return cls(name=row[1], id=row[0])
        

