#!/usr/bin/env python3
# lib/debug.py


import ipdb
from classes.Visit import Visit

from classes.Restaurant import Restaurant
from classes.User import User






Restaurant.drop_table()
Restaurant.create_table()

test = Visit(2, "sample description", "sample date", "sample user", "sample restaurant")
test_2 = Visit(2, "sample description", "sample date", "sample user", "sample restaurant")
test_3 = Visit(2, "sample description", "sample date", "sample user", "sample restaurant")
Visit.create(2, "sample description", "sample date", "sample user", "sample restaurant")

test.save()
test_2.save()
test_3.save()
test_3.delete()

ipdb.set_trace()