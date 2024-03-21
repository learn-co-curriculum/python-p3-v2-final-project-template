#!/usr/bin/env python3
# lib/debug.py

from classes.Visit import Visit

Visit.drop_table()
Visit.create_table()

print(Visit.create(2, "description", "date", "user", "restaurant"))