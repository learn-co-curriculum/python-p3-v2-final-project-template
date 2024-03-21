from __init__ import CURSOR, CONN
from faker import Faker

class Reviewer:
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
        sql = """
            CREATE TABLE IF NOT EXISTS reviewers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            task_list TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def posts_to_review(self):
        # return [post for post in self.posts if not post.reviewed]
        pass