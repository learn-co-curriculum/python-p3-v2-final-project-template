#!/usr/bin/env python3
# lib/debug.py
from rich import print as richp
# from classes.__init__ import CONN, CURSOR
from classes.reviewer import Reviewer
from classes.post import Post
from classes.task import Task


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
    richp(r1)
    richp(r2)
    richp(r3)
    richp(r4)
    richp(r5)
    richp(r6)
    richp(r7)
    richp(r8)
    richp(r9)
    richp(r10)

    
    p1 = Post.create(5200000, 'Text', 'Verified')
    p2 = Post.create(23400000, 'Video', 'Verified')
    p3 = Post.create(6000, 'Picture', 'Caution')
    p4 = Post.create(4500000, 'Picture', 'Debunked')
    p5 = Post.create(66400000, 'Video', 'Verified')
    p6 = Post.create(8000000, 'Text', 'Caution')
    richp(p1)
    richp(p2)
    richp(p3)
    richp(p4)
    richp(p5)
    richp(p6)

if __name__ == '__main__':
    setup_db()
    richp('db seeded!')
    import ipdb; ipdb.set_trace()