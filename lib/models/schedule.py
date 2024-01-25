from models.__init__ import CURSOR, CONN

from models.program import Program
from models.member import Member

class Schedule:

    all = {}

    def __init__(self, program_id, member_id, room, date, start_time, end_time, id=None):
        self.id = id
        self.program_id = program_id
        self.member_id = member_id
        self.room = room
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
    
    def __repr__(self):
        return (
            f"""<Schedule {self.id}
            Program ID: {self.program_id}
            Member ID: {self.member_id}
            Room: {self.room}
            Date (MMDDYY): {self.date}
            Start Time (24hr): {self.start_time}
            End Time (24hr): {self.end_time}
            >"""
        )
    
    @property
    def program_id(self):
        return self._program_id
    @program_id.setter
    def program_id(self, value):
        if isinstance(value, int) and Program.find_by_id(value):
            self._program_id = value
        else:
            raise Exception("program_id must reference a program in the database.")
    
    @property
    def member_id(self):
        return self._member_id
    @member_id.setter
    def member_id(self, value):
        if isinstance(value, int) and Member.find_by_id(value):
            self._member_id = value
        else:
            raise Exception("member_id must reference a member in the database.")
    
    @property
    def room(self):
        return self._room
    @room.setter
    def room(self, value):
        if isinstance(value, str) and 0 < len(value):
            self._room = value
        else:
            raise Exception("room must be of type string and length must be greater than 0.")
    
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) == 6:
            self._date = value
        else:
            raise Exception("date must be of type string and must be 6 digits long.  Format: (MMDDYY).")
    
    @property
    def start_time(self):
        return self._start_time
    @start_time.setter
    def start_time(self, value):
        if isinstance(value, str) and len(value) == 4:
            self._start_time = value
        else:
            raise Exception("start_time must be of type stromg and must be 4 digits long.  Format: 24hr (HHMM).")
    
    @property
    def end_time(self):
        return self._end_time
    @end_time.setter
    def end_time(self, value):
        if isinstance(value, str) and len(value) == 4:
            self._end_time = value
        else:
            raise Exception("end_time must be of type string and must be 4 digits long.  Format: 24hr (HHMM).")
    
    @classmethod
    def create_table(cls):
        # Create a new table to track all Schedule instances
        sql = """
            CREATE TABLE IF NOT EXISTS schedules (
                id INTEGER PRIMARY KEY,
                program_id INTEGER,
                member_id INTEGER,
                room TEXT,
                date TEXT,
                start_time TEXT,
                end_time TEXT,
                FOREIGN KEY (program_id) REFERENCES programs(id)
                FOREIGN KEY (member_id) REFERENCES members(id)
            );
        """

        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS schedules;
        """

        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
            INSERT INTO schedules (program_id, member_id, room, date, start_time, end_time)
            VALUES (?, ?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.program_id, self.member_id, self.room, self.date, self.start_time, self.end_time))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, program_id, member_id, room, date, start_time, end_time):
        schedule = cls(program_id, member_id, room, date, start_time, end_time)
        schedule.save()

        return schedule

    def update(self):
        sql = """
            Update schedules
            SET program_id = ?, member_id = ?, room = ?, date = ?, start_time = ?, end_time = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.program_id, self.member_id, self.room, self.date, self.start_time, self.end_time, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM schedules
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        schedule = cls.all.get(row[0])

        if schedule:
            schedule.program_id = row[1]
            schedule.member_id = row[2]
            schedule.room = row[3]
            schedule.date = row[4]
            schedule.start_time = row[5]
            schedule.end_time = row[6]
        
        else:
            schedule = cls(row[1], row[2], row[3], row[4], row[5], row[6])
            schedule.id = row[0]
            cls.all[schedule.id] = schedule

        return schedule

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM schedules
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def fetch_table(cls):
        pass