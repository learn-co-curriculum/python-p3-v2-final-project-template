#lib/post.py
from __init__ import CURSOR, CONN
from datetime import datetime

CONTENT_TYPES = [
    'Picture',
    'Video',
    'Text'
]

class Post:
    all = {} # dict of all posts in db
    
    def __init__(self, total_interactions, content_type, date, id=None):
        self.id = id
        self.total_interactions = total_interactions
        self.content_type = content_type
        self.created = date
        # self.title = post title, is this needed? or fake link?
        # self.author = author
        # status badges factual, false, use with caution

    def __repr__(self):
        return (
            f'<Post {self.id}: {self.created}, {self.total_interactions}, {self.content_type}>'
        )

    @property
    def total_interactions(self):
        return self._total_interactions
    
    @total_interactions.setter
    def total_interactions(self, total_interactions):
        if not isinstance(total_interactions, int):
            raise ValueError(f'Total Interactions must be an integer.')
        else:
            self._total_interactions = total_interactions

    @property
    def content_type(self):
        return self._content_type
    
    @content_type.setter
    def content_type(self, content_type):
        if not content_type in CONTENT_TYPES:
            raise ValueError(f'Content Type must be in list of CONTENT_TYPES.')
        else:
            self._content_type = content_type

    @property
    def created(self):
        return self._created
    
    @created.setter
    def created(self, created):
        if not :
            raise ValueError(f'Total Interactions must be an integer.')
        else:
            self._created = created


    
    
    #method to check for virality