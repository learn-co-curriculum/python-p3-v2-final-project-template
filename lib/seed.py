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
            print('Created reviewer')
        except Exception as e:
            return e
        
    for _ in range(50):
        try: 
            Post.create(fake.number())
            print('Created post')
        except Exception as e:
            return e

    for _ in range(50):
        try:
            reviewers = Reviewer.get_all()
            posts = Post.get_all()
            Task.create(
                # put things here
            )
            print('Created task')
        except Exception as e:
            return e

if __name__ == "__main__":
    drop_tables()
    print("Tables dropped!")
    create_tables()
    print("Tables created!")
    seed_tables()
    print("Seed data complete!")
    import ipdb; ipdb.set_trace()