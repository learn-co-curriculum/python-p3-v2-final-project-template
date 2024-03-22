from classes.__init__ import CURSOR, CONN
from faker import Faker
class Reviewer:

    fake = Faker()
    print("\nExample 1:")
    for _ in range(2):
        print("Random Word:", fake.word())
        print("Sentence:", fake.sentence())

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
            sql = """
                CREATE TABLE IF NOT EXISTS reviewers (
                id INTEGER PRIMARY KEY,
                name TEXT
                )
            """
            CURSOR.execute(sql)
            CONN.commit()
        except Exception as e:
            CONN.rollback()
            return e
        
    @classmethod
    def drop_table(cls):
        try:
            sql = """
                DROP TABLE IF EXISTS reviewers;
            """
            CURSOR.execute(sql)
            CONN.commit()
        except Exception as e:
            CONN.rollback()
            return e
    
    def save(self):
        try:
            sql = """
                INSERT INTO reviewers (name)
                VALUES (?)
            """
            CURSOR.execute(sql, (self.name,))
            CONN.commit()
            self.id = CURSOR.lastrowid
            return self
        except Exception as e:
            CONN.rollback()
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
            sql = """
                UPDATE reviewers
                SET name = ?
                WHERE id = ?
            """
            CURSOR.execute(sql, (self.name, self.id))
            CONN.commit()
        except Exception as e:
            CONN.rollback()
            return e

    def delete(self):
        try:
            sql = """
                DELETE FROM reviewers
                WHERE id = ?
            """
            CURSOR.execute(sql, (self.id,))
            CONN.commit()
        except Exception as e:
            CONN.rollback()
            return e
        
    def find_by_id(self):
        pass

    def get_all(self):
        pass

    def posts_to_review(self):
        # return [post for post in self.posts if not post.reviewed]
        pass