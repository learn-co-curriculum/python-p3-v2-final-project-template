#!/usr/bin/env python3
# lib/debug.py
import ipdb; 
from models.__init__ import CURSOR, CONN

from models.program import Program
from models.schedule import Schedule
from models.location import Location
from models.trainer import Trainer
from models.member import Member

print("In Debugger!")

Trainer.drop_table()
Location.drop_table()
Program.drop_table()
Member.drop_table()
Schedule.drop_table()

Trainer.create_table()
Location.create_table()
Program.create_table()
Member.create_table()
Schedule.create_table()

t1 = Trainer.create("Bob", "Thornton")
t2 = Trainer.create("Jill", "Thomas")
t3 = Trainer.create("Andrew", "Lincoln")


L1 = Location.create("Chicago")
L2 = Location.create("Detroit")

p1 = Program.create(2, 1, "Boxing", "Basic")
p2 = Program.create(2, 2, "Zumba", "Premium")
p3 = Program.create(2, 2, "Spinning", "Basic")
p4 = Program.create(1, 1, "Strength Training", "Premium")

m1 = Member.create("Jeffrey", "Davis", "Basic")
m2 = Member.create("Katie", "Nowicki", "Premium")
m3 = Member.create("Hadil", "Hijazi", "Premium")

s1 = Schedule.create(1, 2, "101", "012524", "0900", "1000")

ipdb.set_trace()