#!/usr/bin/env python3
# lib/debug.py

from classes.User import User

User.drop_table()
User.create_table()

User.create('Christian')










