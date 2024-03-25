#!/usr/bin/env python3
# lib/debug.py
# from rich import print
from rich.console import Console
from rich import inspect
import rich
# from classes.__init__ import CONN, CURSOR
from classes.reviewer import Reviewer
from classes.post import Post
from classes.task import Task

console = Console()

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
    console.print(r1)
    console.print(r2)
    console.print(r3)
    console.print(r4)
    console.print(r5)
    console.print(r6)
    console.print(r7)
    console.print(r8)
    console.print(r9)
    console.print(r10)

    p1 = Post.create(5200000, 'Text', 'Verified')
    p2 = Post.create(23400000, 'Video', 'Verified')
    p3 = Post.create(6000, 'Picture', 'Caution')
    p4 = Post.create(4500000, 'Picture', 'Debunked')
    p5 = Post.create(66400000, 'Video', 'Verified')
    p6 = Post.create(8000000, 'Text', 'Caution')
    console.print(p1)
    console.print(p2)
    console.print(p3)
    console.print(p4)
    console.print(p5)
    console.print(p6, style='bold underline blue')

if __name__ == '__main__':
    setup_db()
    print('db seeded!')
    import ipdb; ipdb.set_trace()
    inspect(rich)