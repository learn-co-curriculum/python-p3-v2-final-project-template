#!/usr/bin/env python3
#lib/post.py
from classes.__init__ import CURSOR, CONN
from datetime import datetime

CONTENT_TYPES = [
    'Picture',
    'Video',
    'Text',
]

FACT_CHECKED = [
    'Verified',
    'Debunked',
    'Caution'
]

class Post:
    all = {} # dict of all posts in db
    
    def __init__(self, total_interactions, content_type, id=None, review_badge=None):
        self.total_interactions = total_interactions
        self.content_type = content_type
        self.created_at = datetime.now()
        self.id = id
        self.review_badge = review_badge # All posts set to None until reviewed

    def __repr__(self):
        return (
            f'<Post {self.id}: {self.created_at}, {self.total_interactions}, {self.content_type}>, {self.review_badge}'
        )

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

    @property
    def review_badge(self):
        return self._review_badge
    
    @review_badge.setter
    def review_badge(self, new_review_badge):
        if not new_review_badge in FACT_CHECKED:
            raise ValueError(f"'review_badge' must be in list of FACT_CHECKED.")
        else:
            self._review_badge = new_review_badge

    #! Association Methods go here
    #method to check for virality

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
                        review_badge TEXT
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

    @classmethod
    def create(cls, total_interactions, content_type, review_badge):
        try:
            with CONN:
                new_post = cls(total_interactions, content_type, review_badge)
                new_post.save()
            return new_post
        except Exception as e:
            return e

    @classmethod
    def new_from_db(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    SELECT * FROM posts
                    ORDER BY id DESC
                    LIMIT 1;
                    """
                )
                row = CURSOR.fetchone()
            return cls._create_post_from_row(row) if row else None
        except Exception as e:
            return e

    @classmethod
    def get_all(cls):
        try:
            CURSOR.execute(
                """
                SELECT * FROM posts;
                """
            )
            rows = CURSOR.fetchall()
            return [cls(row[1], row[2], row[3], row[0]) for row in rows]
        except Exception as e:
            return e

    @classmethod
    def find_by_id(cls, id):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    SELECT * FROM posts
                    WHERE id is ?;
                    """,
                    (id,),
                )
                row = CURSOR.fetchone()
            return cls._create_post_from_row(row) if row else None
        except Exception as e:
            return e

    @classmethod # datetime helper, seperates responsibility of parsing datetime string
    def _create_post_from_row(cls, row):
        if row:
            created_at = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S")
            return cls(row[1], row[2], created_at, row[4], row[0])
        return None


    #! ORM Instance Methods
    def save(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    INSERT INTO posts (total_interactions, content_type, created_at)
                    VALUES (?, ?, ?);
                    """,
                    (self.total_interactions, self.content_type, self.created_at, self.review_badge)
                )
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
                    SET total_interactions = ?, content_type = ?, review_badge = ?
                    WHERE id = ?
                    """,
                    (self.total_interactions, self.content_type, self.review_badge, self.id)
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
                    (self.id,),
                )
                CONN.commit()
                del type(self).all[self.id]
                self.id = None
            return self
        except Exception as e:
            return e
