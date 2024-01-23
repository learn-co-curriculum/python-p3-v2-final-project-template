import sqlite3

CONN = sqlite3.connect("lib/gym.db")
CURSOR = CONN.cursor()

class Program:

    all = []

    def __init__(self, location, trainer, exercise, membership_required="Premium", id=None):
        self.id = id
        self.location = location
        self.trainer = trainer
        self.exercise = exercise
        self.membership_required = membership_required

        Program.all.append(self)
    
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
        # Create a new table to track all Program instances
        sql = """
            CREATE TABLE IF NOT EXISTS programs (
                id INTEGER PRIMARY KEY,
                trainer_id INTEGER,
                exercise_id INTEGER,
                membership_required TEXT,
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
            INSERT INTO programs (trainer_id, exercise_id, membership_required)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.trainer.id, self.exercise.id, self.membership_required))
        CONN.commit()
        self.id = CURSOR.lastrowid
    
    # @classmethod
    # def create(cls, )
    
    @classmethod
    def fetch_table(cls):
        pass

    # def display_info(self):
    #     location_info = f"Location: {self.location.name}"
    #     trainer_info = f"Trainer: {self.trainer.name}"
    #     exercise_info = f"Exercise: {self.exercise.name}"
    #     membership_info = f"Membership Type: {self.membership_type}"

    #     print(f"Premium Information:\n{location_info}\n{trainer_info}\n{exercise_info}\n{membership_info}")