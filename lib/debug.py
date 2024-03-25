#!/usr/bin/env python3
# lib/debug.py
from rich import print
# from classes.__init__ import CONN, CURSOR
from classes.post import Post
from classes.task import Task
from classes.reviewer import Reviewer


def setup_db():
    Task.drop_table()
    Reviewer.drop_table()
    Post.drop_table()

    Reviewer.create_table()
    Post.create_table()
    Task.create_table()

    # create seed data
    r1 = Reviewer.create('Jasmine Patel')
    r2 = Reviewer.create('Liam Thompson')
    r3 = Reviewer.create('Olivia Jensen')
    r4 = Reviewer.create('Bob Ross')
    r5 = Reviewer.create('Ethan Chang')
    r6 = Reviewer.create('Noah Martinez')
    r7 = Reviewer.create('Ava Nguyen')
    r8 = Reviewer.create('Lucas Rodriguez')
    r9 = Reviewer.create('Isabella Khan')
    r10 = Reviewer.create('Mason Kim')
    
    p1 = Post.create(5200000, 'Text', 'Debunked')
    p2 = Post.create(23400000, 'Video', 'Verified')
    p3 = Post.create(6000, 'Picture', None)
    p4 = Post.create(4500000, 'Picture', 'Debunked')
    p5 = Post.create(66400000, 'Video', None)
    p6 = Post.create(8000000, 'Text', 'Caution')

if __name__ == '__main__':
    setup_db()
    print('db seeded!')
    import ipdb; ipdb.set_trace()