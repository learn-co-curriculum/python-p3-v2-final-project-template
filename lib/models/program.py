import sqlite3
from models.__init__ import CONN, CURSOR
from models.location import Location
from models.trainer import Trainer
from models.exercise import Exercise


CONN = sqlite3.connect("lib/gym.db")
CURSOR = CONN.cursor()


class Program:
    all = []

    def __init__(self, location, trainer, exercise, membership_required="Basic", id=None):
        self.id = id
        self.location = location
        self.trainer = trainer
        self.exercise = exercise
        self.membership_required = membership_required
        Program.all.append(self)

    def __repr__(self):
       return (f"<Program {self.id}: Location: {self.location.city}, Trainer: {self.trainer.first_name} {self.trainer.last_name}, Exercise: {self.exercise.name}, Membership Required: {self.membership_required}>") 
    
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, value):
        from models.location import Location

        if isinstance(value, Location):
            self._location = value
        else:
            raise Exception("location must be of type class Location.")
    
    @property
    def trainer(self):
        return self._trainer
    
    @trainer.setter
    def trainer(self, value):
        from models.trainer import Trainer

        if isinstance(value, Trainer):
            self._trainer = value
        else:
            raise Exception("trainer must be of type class Trainer.")
    
    @property
    def exercise(self):
        return self._exercise
    
    @exercise.setter
    def exercise(self, value):
        from models.exercise import Exercise

        if isinstance(value, Exercise):
            self._exercise = value
        else:
            raise Exception("exercise must be of type class Exercise.")
    
    @property
    def membership_required(self):
        return self._membership_required
    
    @membership_required.setter
    def membership_required(self, value):
        if isinstance(value, str) and (value.lower() == "basic" or value.lower() == "premium"):
            self._membership_required = value
        else:
            raise Exception("membership_required must be of type string and must be either basic or premium.")
    
    @classmethod
    def create_table(cls):
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
        if self.id is None:
            sql = "INSERT INTO programs (location_id, trainer_id, exercise_id, membership_required) VALUES (?, ?, ?, ?)"
            CURSOR.execute(sql, (self.location.id, self.trainer.id, self.exercise.id, self.membership_required))
            CONN.commit()
            self.id = CURSOR.lastrowid
        else:
            sql = "UPDATE programs SET location_id = ?, trainer_id = ?, exercise_id = ?, membership_required = ? WHERE id = ?"
            CURSOR.execute(sql, (self.location.id, self.trainer.id, self.exercise.id, self.membership_required, self.id))
            CONN.commit()

    @classmethod
    def get_all_programs(cls):
        sql = """
            SELECT p.id, p.location_id, p.trainer_id, p.exercise_id, p.membership_required, e.name, l.city, t.first_name, t.last_name
            FROM programs p
            JOIN exercises e ON p.exercise_id = e.id
            JOIN locations l ON p.location_id = l.id
            JOIN trainers t ON p.trainer_id = t.id
            ORDER BY e.name, l.city, t.first_name, t.last_name, p.membership_required
        """
        return [cls.new_from_db(one_row) for one_row in CURSOR.execute(sql).fetchall()]


    @classmethod
    def delete_by_id(cls, id):
        sql = "DELETE FROM programs WHERE id = ?"
        CURSOR.execute(sql, (id,))
        CONN.commit()

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM programs WHERE id = ?"
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        if row:
            return cls.new_from_db(row)
        return None


    # Assuming new_from_db constructs a Program instance from a database row
    @classmethod
    def new_from_db(cls, row):
        location = Location.find_by_id(row[1])
        trainer = Trainer.find_by_id(row[2])
        exercise = Exercise.find_by_id(row[3])
        return cls(location=location, trainer=trainer, exercise=exercise, membership_required=row[4], id=row[0])
