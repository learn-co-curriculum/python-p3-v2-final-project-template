
import sqlite3

CONN = sqlite3.connect("lib/gym.db")
CURSOR = CONN.cursor()

from models.__init__ import CURSOR, CONN

from models.location import Location
from models.trainer import Trainer

class Program:

    all = {}

    def __init__(self, location_id, trainer_id, exercise_name, membership_required, id=None):
        self.id = id
        self.location_id = location_id
        self.trainer_id = trainer_id
        self.exercise_name = exercise_name
        self.membership_required = membership_required
        Program.all.append(self)


    def __repr__(self):
        return (
            f"""<Program {self.id}
            Exercise Name: {self.exercise_name}
            Location ID: {self.location_id}
            Trainer ID: {self.trainer_id}
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
    def exercise_name(self):
        return self._exercise_name
    @exercise_name.setter
    def exercise_name(self, value):
        if isinstance(value, str) and 0 < len(value):
            self._exercise_name = value
        else:
            raise Exception("exercise_name must be of type string and longer than 0 characters.")
    
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
                exercise_name TEXT,
                membership_required TEXT,
                FOREIGN KEY (location_id) REFERENCES locations(id),
                FOREIGN KEY (trainer_id) REFERENCES trainers(id)
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
            INSERT INTO programs (location_id, trainer_id, exercise_name, membership_required)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.location_id, self.trainer_id, self.exercise_name, self.membership_required))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, location_id, trainer_id, exercise_name, membership_required):
        program = cls(location_id, trainer_id, exercise_name, membership_required)
        program.save()

        return program
    
    def update(self):
        sql = """
            Update programs
            SET location_id = ?, trainer_id = ?, exercise_name = ?, membership_required = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.location_id, self.trainer_id, self.exercise_name, self.membership_required, self.id))
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
            program.exercise_name = row[3]
            program.membership_required = row[4]
        
        else:
            program = cls(row[1], row[2], row[3], row[4])
            program.id = row[0]
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

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM programs;
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        programs = []
        for row in rows:
            program = cls.instance_from_db(row)
            programs.append(program)
        return programs
    
    # @classmethod
    # def get_all_programs(cls):
    #     sql = """
    #         SELECT p.id, t.name, e.name, l.name, p.membership_required
    #         FROM programs p
    #         JOIN trainers t ON p.trainer_id = t.id
    #         JOIN exercises e ON p.exercise_id = e.id
    #         JOIN locations l ON p.location_id = l.id;
    #     """
    #     CURSOR.execute(sql)
    #     programs = CURSOR.fetchall()
    #     return programs
   
    #     type(self).all[self.id] = self
