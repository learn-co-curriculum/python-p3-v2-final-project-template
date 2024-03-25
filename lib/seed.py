#!/user/bin/env python3
from faker import Faker

from classes.__init__ import CONN, CURSOR
from classes.post import Post
from classes.reviewer import Reviewer
from classes.task import Task

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
            Reviewer.create(fake.name())
            print('Created reviewers')
        except Exception as e:
            return e

    # for _ in range(6):
    #     try:
    #         # Post.create(fake.number)
    #     except Exception as e:
    #         return e


    # Create seed data
    # task_list = Task.create("Task List",)
    # Reviewer.create
# seed_database()


if __name__ == "__main__":
    drop_tables()
    print("Tables dropped!")
    create_tables()
    print("Tables created!")
    seed_tables()
    print("Seed data complete!")
    import ipdb; ipdb.set_trace()