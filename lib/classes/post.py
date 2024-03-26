#!/usr/bin/env python3
#lib/classes.post.py
from classes.__init__ import CURSOR, CONN
from datetime import datetime

CONTENT_TYPES = [
    'Picture',
    'Video',
    'Text'
]

FACT_CHECKED = [
    'Verified',
    'Debunked',
    'Caution'
]

class Post:
    all = {} # dict of all posts in db

    def __init__(self, total_interactions, content_type, id=None):
        self.total_interactions = total_interactions
        self.content_type = content_type
        self.created_at = datetime.now()
        self.review_badge = None # All posts set to None until reviewed
        self.is_viral = self.calculate_virality(total_interactions)
        self.id = id

    def __repr__(self):
        return (
            f"""<Post {self.id}: Creation Date: {self.created_at}, Interactions: {self.total_interactions}, Content Type: {self.content_type}, Viral: {self.is_viral}, Review Badge: {self.review_badge}>"""
        )

    @staticmethod # belongs class, not its instances. can be called without creating an instance
    def calculate_virality(total_interactions):
        return total_interactions >= 3500000

    #! Attributes and Props
    @property
    def total_interactions(self):
        return self._total_interactions

    @total_interactions.setter
    def total_interactions(self, total_interactions):
        if not isinstance(total_interactions, int):
            raise ValueError(f"'total_interactions' must be an integer.")
        else:
            self._total_interactions = total_interactions

    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        if not content_type in CONTENT_TYPES:
            raise ValueError(f"'content_type' must be in list of CONTENT_TYPES.")
        else:
            self._content_type = content_type

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        if not isinstance(value, datetime):
            raise TypeError(f"'created_at' must be a valid datetime object.")
        else:
            self._created_at = value

    def review_badge(self, new_review_badge):
        if not new_review_badge in FACT_CHECKED:
            raise ValueError(f"'review_badge' must be in list of FACT_CHECKED.")
        else:
            self.review_badge = new_review_badge

    def is_viral(self, total_interactions):
        if total_interactions >= 3500000:
            self.is_viral = True
        else:
            self.is_viral = False

    def task(self):
        from classes.task import Task

        try:
            with CONN:
                CURSOR.execute(
                    """
                    SELECT * FROM tasks
                    WHERE post_id = ?
                    """,
                    (self.id,),
                )
                rows = CURSOR.fetchall()
                return [Task(row[1], row[2], row[3], row[4], row[5], row[0]) for row in rows]
        except Exception as e:
            return e
    # ! if has task, get/show task status

    #! ORM Class Methods
    @classmethod
    def create_table(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    CREATE TABLE IF NOT EXISTS posts (
                        id INTEGER PRIMARY KEY,
                        total_interactions INTEGER,
                        content_type TEXT,
                        created_at TEXT,
                        review_badge TEXT,
                        is_viral TEXT
                    );
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
                    DROP TABLE IF EXISTS posts;
                    """
                )
        except Exception as e:
            return e

    @classmethod #! minimum fields: interactions and content type -- optional attr
    def create(cls, total_interactions, content_type, review_badge):
        try:
            with CONN:
                new_post = cls(total_interactions, content_type, review_badge)
                new_post.save()
            return new_post
        except Exception as e:
            return e

    @classmethod #create new instantance of Post based on info in db
    def new_from_db(cls, row):
        try:
            post = cls(row[1], row[2], row[3], row[4], row[5], row[0])
            cls.all[post.id] = post
            return post
        except Exception as e:
            return e

    @classmethod
    def get_all(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    SELECT * FROM posts;
                    """
                )
                rows = CURSOR.fetchall()
                return [cls(row[1], row[2], row[3], row[4], row[5], row[0]) for row in rows]
        except Exception as e:
            return e

    @classmethod
    def find_by_id(cls, id):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    SELECT * FROM posts
                    WHERE id = ?;
                    """,
                    (id,)
                )
                row = CURSOR.fetchone()
            return cls._create_post_from_row(row) if row else None
        except Exception as e:
            return e

    @classmethod
    def find_by(cls, attr, val):
        try:
            CURSOR.execute(
                f"""
                SELECT * FROM posts
                WHERE {attr} = ?;
                """,
                (val,)
            )
            row = CURSOR.fetchone()
            return cls._create_post_from_row(row) if row else None
        except Exception as e:
            return e

    @classmethod # datetime helper. Parses datetime str
    def _create_post_from_row(cls, row):
        if row:
            created_at = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S")
            return cls(row[1], row[2], created_at, row[4], row[5], row[0])
        return None

    #! ORM Instance Methods
    def save(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    INSERT INTO posts (total_interactions, content_type, created_at, review_badge, is_viral)
                    VALUES (?, ?, ?, ?, ?);
                    """,
                    (self.total_interactions, self.content_type, self.created_at, self.review_badge, self.is_viral)
                )
                CONN.commit()
                self.id = CURSOR.lastrowid
                type(self).all[self.id] = self
            return self
        except Exception as e:
            return e

    def update(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    UPDATE posts 
                    SET total_interactions = ?, content_type = ?, review_badge = ?, is_viral = ?
                    WHERE id = ?
                    """,
                    (self.total_interactions, self.content_type, self.review_badge, self.is_viral, self.id)
                )
                CONN.commit()
                type(self).all[self.id] = self
                return self
        except Exception as e:
            return e

    def delete(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    DELETE FROM posts
                    WHERE id = ?
                    """,
                    (self.id,)
                )
                CONN.commit() #rm memoized obj
                del type(self).all[self.id]
                self.id = None #nullify id
            return self
        except Exception as e:
            return e
