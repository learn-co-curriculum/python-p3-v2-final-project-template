from models.__init__ import CURSOR, CONN

class Schedule:

    all = []

    def __init__(self, program, member, room, date, start_time, end_time, id=None):
        self.id = id
        self.program = program
        self.member = member
        self.room = room
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

        Schedule.all.append(self)
    
    @property
    def program(self):
        return self._program
    @program.setter
    def program(self, value):
        from models.program import Program

        if isinstance(value, Program):
            self._program = value
        else:
            raise Exception("program must be of type class Program.")
    
    @property
    def member(self):
        return self._member
    @member.setter
    def member(self, value):
        from models.member import Member

        if isinstance(value, Member):
            self._member = value
        else:
            raise Exception("member must be of type class Member.")
    
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
        if isinstance(value, int) and len(str(value)) == 6:
            self._date = value
        else:
            raise Exception("date must be of type integer and must be 6 digits long.  Format: (MMDDYY).")
    
    @property
    def start_time(self):
        return self._start_time
    @start_time.setter
    def start_time(self, value):
        if isinstance(value, int) and len(str(value)) == 4:
            self._start_time = value
        else:
            raise Exception("start_time must be of type integer and must be 4 digits long.  Format: (HHMM).")
    
    @property
    def end_time(self):
        return self._end_time
    @end_time.setter
    def end_time(self, value):
        if isinstance(value, int) and len(str(value)) == 4:
            self._end_time = value
        else:
            raise Exception("end_time must be of type integer and must be 4 digits long.  Format: (HHMM).")
    
    @classmethod
    def create_table(cls):
        # Create a new table to track all Schedule instances
        sql = """
            CREATE TABLE IF NOT EXISTS schedules (
                id INTEGER PRIMARY KEY,
                program_id INTEGER,
                room TEXT,
                date INTEGER,
                start_time INTEGER,
                end_time INTEGER,
                FOREIGN KEY (program_id) REFERENCES programs(id)
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
            INSERT INTO schedules (program_id, room, date, start_time, end_time)
            VALUES (?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.program, self.room, self.date, self.start_time, self.end_time,))
        CONN.commit()
        self.id = CURSOR.lastrowid
    




    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM locations
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def fetch_table(cls):
        pass