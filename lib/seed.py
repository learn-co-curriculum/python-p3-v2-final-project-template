#!/user/bin/env python3

from classes.__init__ import CONN, CURSOR
from classes.post import Post
from classes.reviewer import Reviewer
from classes.task import Task
from faker import Faker

fake = Faker()


def drop_tables():
    Task.drop_table()
    Reviewer.drop_table()
    Post.drop_table()
    
def create_tables():
    Post.create_table()
    Reviewer.create_table()
    Task.create_table()

def seed_tables():
    for _ in range(10):
        try:
            reviewers = Reviewer.get_all()

        except Exception as e:
            return e


    # Create seed data
    # task_list = Task.create("Task List",)
    Reviewer.create
seed_database()
