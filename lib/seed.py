#!/user/bin/env python3

from classes.__init__ import CONN, CURSOR
from classes.post import Post
from classes.reviewer import Reviewer
from classes.task import Task

def seed_database():
    Post.drop_table()
    Reviewer.drop_table()
    Task.drop_table()
    Post.create_table()
    Reviewer.create_table()
    Task.create_table()

    # Create seed data
    

seed_database()
