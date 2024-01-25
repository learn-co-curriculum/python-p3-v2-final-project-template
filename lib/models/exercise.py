from models.__init__ import CURSOR, CONN

class Exercise:

    all = {}

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

    def display_info(self):
        print(f"Exercise Name: {self.name}")

    def add_exercise(self):
        query = "INSERT INTO exercise (name) VALUES (?);"
        values = (self.name,)
        self.CURSOR.execute(query, values)
        self.CONN.commit()

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
        type(self).all[self.id] = self

    
    @classmethod
    def create(cls, name):
        exercise = cls(name)
        exercise.save()

        return exercise

    def update(self):
        sql = """
            UPDATE exercises
            SET name = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM exercises
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None
    
    @classmethod
    def instance_from_db(cls, row):
        exercise = cls.all.get(row[0])

        if exercise:
            exercise.name = row[1]
        
        else:
            exercise = cls(row[1])
            exercise.id = row[0]
            cls.all[exercise.id] = exercise

        return exercise
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM exercises
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        return cls.instance_from_db(row) if row else None


    @classmethod
    def new_from_db(cls, row):
        return cls(name=row[1], id=row[0])
        sql = """
            SELECT * FROM exercises
            WHERE name = ?
            LIMIT 1;
        """
        CURSOR.execute(sql, (name,))
        row = CURSOR.fetchone()
        if row:
            return cls.instance_from_db(row)  # Assuming new_form_db constructs a Trainer instance
        else:
            return None
    