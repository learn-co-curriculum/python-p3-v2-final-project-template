#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.Course import Course
import ipdb

def reset_database():
    Course.drop_table()
    Course.create_table()

    course = Course.create("Yeji", "A", "fall")

reset_database()

ipdb.set_trace()
