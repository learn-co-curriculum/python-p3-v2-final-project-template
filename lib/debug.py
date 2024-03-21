#!/usr/bin/env python3
# lib/debug.py

from classes.Visit import Visit

Visit.drop_table()
Visit.create_table()

test = Visit(2, "sample description", "sample date", "sample user", "sample restaurant")
test_2 = Visit(2, "sample description", "sample date", "sample user", "sample restaurant")
test_3 = Visit(2, "sample description", "sample date", "sample user", "sample restaurant")
Visit.create(2, "sample description", "sample date", "sample user", "sample restaurant")

test.save()
test_2.save()
test_3.save()
test_3.delete()

