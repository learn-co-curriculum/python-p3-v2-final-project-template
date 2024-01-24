#!/usr/bin/env python3
# lib/debug.py
import ipdb; 
from models.__init__ import CURSOR, CONN

from models.program import Program
from models.schedule import Schedule
from models.location import Location
from models.trainer import Trainer
from models.exercise import Exercise
from models.member import Member

print("In Debugger!")

t1 = Trainer("Bob", "Thornton")
t2 = Trainer("Jill", "Thomas")
t3 = Trainer("Andrew", "Lincoln")

e1 = Exercise("Boxing")
e2 = Exercise("Zumba")
e3 = Exercise("Rowing")

L1 = Location("Chicago")

# p1 = Program(L1, t1, e1, "Basic")
# p2 = Program(L2, t2, e2, "Premium")
# p3 = Program(L1, t3, e1, "Premium")
# p4 = Program(L1, t3, e3, "Premium")

m1 = Member("Jeffrey", "Davis", "Basic")
m2 = Member("Katie", "Nowicki", "Premium")
m3 = Member("Hadil", "Hijazi", "Premium")

# print(p1)
# print(p1.location.city)
# print(p1.trainer.first_name)
# print(p1.exercise.name)
# print(p1.membership_required)

Trainer.drop_table()
Exercise.drop_table()
Location.drop_table()
Program.drop_table()
Member.drop_table()

Trainer.create_table()
Exercise.create_table()
Location.create_table()
Program.create_table()
Member.create_table()

L1.save()
L1.create("Milwaikee")

# t1.save()
# e1.save()
# L1.save()
# p1.save()
# m2.save()

# t2.save()
# e2.save()
# L2.save()
# p2.save()
# m1.save()

# t3.save()
# e3.save()
# L3.save()
# p3.save()
# m3.save()

ipdb.set_trace()