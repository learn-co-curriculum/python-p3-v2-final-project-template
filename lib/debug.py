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

# t1 = Trainer.create("Bob", "Thornton")
# t2 = Trainer.create("Jill", "Thomas")
# t3 = Trainer.create("Andrew", "Lincoln")


# e1 = Exercise.create("Boxing")
# e2 = Exercise.create("Zumba")
# e3 = Exercise.create("Rowing")

# L1 = Location.create("Chicago")
# L2 = Location.create("Detroit")

# p1 = Program.create(1, 2, 1)
# p2 = Program.create(2, 2, 2)
# p3 = Program.create(1, 2, 2)
# p4 = Program.create(1, 3, 1, "Premium")

# m1 = Member.create("Jeffrey", "Davis", "Basic")
# m2 = Member.create("Katie", "Nowicki", "Premium")
# m3 = Member.create("Hadil", "Hijazi", "Premium")

ipdb.set_trace()