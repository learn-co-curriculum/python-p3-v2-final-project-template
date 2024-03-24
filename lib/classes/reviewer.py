from classes.__init__ import CURSOR, CONN
from faker import Faker
class Reviewer:
    all = {}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name
        self.posts = []
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        elif len(name) <= 2:
            raise ValueError("Name must be at least two chars inclusive.")
        else:
            self._name = name

    def __repr__(self):
        return f"<Reviewer {self.id}: {self.name}>"

    @classmethod
    def create_table(cls):
        try:
            with CONN:
                CURSOR.executescript(
                    """
                    BEGIN;
                    CREATE TABLE IF NOT EXISTS reviewers (
                        id INTEGER PRIMARY KEY,
                        name TEXT
                    );
                    CREATE INDEX idx_full_name ON reviewers (full_name);
                    COMMIT
                    """
                )
        except Exception as e:
            return e
        
    @classmethod
    def drop_table(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    DROP TABLE IF EXISTS reviewers;
                    """
                )
        except Exception as e:
            return e
    
    def save(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    INSERT INTO reviewers (name)
                    VALUES (?)
                    """
                )
                CONN.commit()
                self.id = CURSOR.lastrowid
                type(self).all[self.id] = self
                return self
        except Exception as e:
            return e

    @classmethod
    def create(cls, name):
        try:
            reviewer = cls(name)
            rev = reviewer.save()
            return rev
        except Exception as e:
            return e

    def update(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    UPDATE reviewers
                    SET name = ?
                    WHERE id = ?
                    """,
                    (self.name, self.id),
                )
        except Exception as e:
            return e

    def delete(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    DELETE FROM reviewers
                    WHERE id = ?
                    """,
                    (self.id,),
                )
            CONN.commit()
            del type(self).all[self.id]
            self.id = None
        except Exception as e:
            return e
        

    @classmethod
    def find_by_id(cls, id):
        try:
            CURSOR.execute(
                f"""
                SELECT * FROM reviewers
                WHERE id is ?;
            """,
            (id,),
            )
            row = CURSOR.fetchone()
            return cls(row[1]) if row else None
        except Exception as e:
            return e

    @classmethod
    def get_all(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    SELECT * FROM reviewers;
                    """
                )
                rows = CURSOR.fetchall()
                return [cls(row[1]) for row in rows]
        except Exception as e:
            return e

    def tasks(self):
        from classes.task import Task

        try:
            with CONN:
                CURSOR.execute(
                    """
                        SELECT * FROM tasks
                        WHERE reviewer_id = ?
                    """,
                    (self.id,),
                )
                rows = CURSOR.fetchall()
                # return [Task()]
        except Exception as e:
            return e
        pass