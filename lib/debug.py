#!/usr/bin/env python3
# lib/debug.py
import ipdb

from models.__init__ import CONN, CURSOR
from models.author import Author
from models.post import Post

# Author.drop_table()
# Author.create_table()
# Post.drop_table()
# Post.create_table()
# p1 = Post("Big whale", "Big whales are very big", "nature", "Grant")
# p2 = Post("Small whale", "Small whales are very small", "nature", "Grant")
# p3 = Post("Panthers", "Panthers are trash", "sports", "Dan")
a1 = Author("Max", "cars")


ipdb.set_trace()
