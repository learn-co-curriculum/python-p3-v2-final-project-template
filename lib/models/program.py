from models.__init__ import CURSOR, CONN
from models.location import Location
from models.exercise import Exercise
from models.trainer import Trainer

class Program:

    all = {}

    def __init__(self, location_id, trainer_id, exercise_id, membership_required="Basic", id=None):

        self.id = id
        self.location_id = location_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.membership_required = membership_required

    def __repr__(self):
        return (
            f"""<Program {self.id}
            Location ID: {self.location_id}
            Trainer ID: {self.trainer_id}
            Exercise ID: {self.exercise_id}
            Membership Level Needed: {self.membership_required}>"""
        )
    
    @property
    def location_id(self):
        return self._location_id
    @location_id.setter
    def location_id(self, value):
        if isinstance(value, int) and Location.find_by_id(value):
            self._location_id = value
        else:
            raise Exception("location_id must reference a location in the database.")
    
    @property
    def trainer_id(self):
        return self._trainer_id
    @trainer_id.setter
    def trainer_id(self, value):
        if isinstance(value, int) and Trainer.find_by_id(value):
            self._trainer_id = value
        else:
            raise Exception("trainer_id must reference a trainer in the database.")
    
    @property
    def exercise_id(self):
        return self._exercise_id
    @exercise_id.setter
    def exercise_id(self, value):
        if isinstance(value, int) and Exercise.find_by_id(value):
            self._exercise_id = value
        else:
            raise Exception("exercise_id must reference an exercise in the database.")
    
    @property
    def membership_required(self):
        return self._membership_required
    @membership_required.setter
    def membership_required(self, value):
        if value.lower() in ["basic", "premium"]:
            self._membership_required = value
        else:
            raise Exception("membership_required be either basic or premium.")
    
    @classmethod
    def create_table(cls):
        # Create a new table to track all Program instances
        sql = """
            CREATE TABLE IF NOT EXISTS programs (
                id INTEGER PRIMARY KEY,
                location_id INTEGER,
                trainer_id INTEGER,
                exercise_id INTEGER,
                membership_required TEXT,
                FOREIGN KEY (location_id) REFERENCES locations(id),
                FOREIGN KEY (trainer_id) REFERENCES trainers(id),
                FOREIGN KEY (exercise_id) REFERENCES exercises(id)
            );
        """

        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS programs;
        """

        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
            INSERT INTO programs (location_id, trainer_id, exercise_id, membership_required)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.location_id, self.trainer_id, self.exercise_id, self.membership_required))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, location_id, trainer_id, exercise_id, membership_required="Basic"):
        program = cls(location_id, trainer_id, exercise_id, membership_required)
        program.save()

        return program
    
    def update(self):
        sql = """
            Update programs
            SET location_id = ?, trainer_id = ?, exercise_id = ?, membership_required = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.location_id, self.trainer_id, self.exercise_id, self.membership_required, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM programs
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None
    
    @classmethod
    def instance_from_db(cls, row):
        program = cls.all.get(row[0])

        if program:
            program.location_id = row[1]
            program.trainer_id = row[2]
            program.exercise_id = row[3]
            program.membership_required = row[4]
        
        else:
            program = cls(row[1], row[2], row[3], row[4])
            program.id = row[4]
            cls.all[program.id] = program
        
        return program
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM programs
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def fetch_table(cls):
        pass