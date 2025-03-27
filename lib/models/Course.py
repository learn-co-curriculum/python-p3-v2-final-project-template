from models.__init__ import CURSOR, CONN

class Course:
    all = {}

    def __init__(self, teacher, classname, term, id=None):
        self.id = id
        self.teacher = teacher
        self.classname = classname
        self.term = term

    def __repr__(self):
        return f"<Course {self.id}: {self.teacher}, {self.classname},{self.term} >"

    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, teacher):
        if isinstance(teacher, str) and len(teacher)>0:
            self._teacher = teacher
        else:
            raise ValueError(
                "teacher must be a non-empty string"
            )
    @property
    def classname(self):
        return self._classname

    @classname.setter
    def classname(self, classname):
        if isinstance(classname, str) and len(classname)>0:
            self._classname = classname
        else:
            raise ValueError(
                "classname must be a non-empty string"
            )
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY,
            teacher TEXT,
            classname TEXT,
            term TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS courses;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
    
        sql = """
            INSERT INTO courses (teacher, classname, term)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.teacher, self.classname, self.term))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, teacher, classname, term):
        course = cls(teacher, classname, term)
        course.save()
        return course

    def update(self):
        sql = """
            UPDATE courses
            SET teacher = ?, classname = ?, term = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.teacher, self.classname, self.term, self.id))
        CONN.commit()

    def delete(self):
        

        sql = """
            DELETE FROM courses
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):

        course = cls.all.get(row[0])
        if course:
            course.teacher = row[1]
            course.classname = row[2]
            course.term = row[3]

        else:
            course = cls(row[1], row[2], row[3])
            course.id = row[0]
            cls.all[course.id] = course
        return course

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM courses
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM courses
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, classname):
        sql = """
            SELECT *
            FROM courses
            WHERE classname is ?
        """

        row = CURSOR.execute(sql, (classname,)).fetchone()
        return cls.instance_from_db(row) if row else None

    