#!/usr/bin/env python3
# lib/debug.py
import ipdb; 

from models.program import Program
from models.schedule import Schedule
from models.location import Location
from models.trainer import Trainer
from models.exercise import Exercise
from models.member import Member

print("In Debugger!")

L1 = Location("Chicago")
t1 = Trainer("Bob", "Thornton")
e1 = Exercise("Boxing")

m1= Member("Jeffrey", "Davis", "Basic")
m2= Member("Katie", "Nowicki", "Premium")
m3= Member("Hadil", "Hijazi", "Premium")

Member.create_table()
Program.create_table()
Exercise.create_table()
Location.create_table()

# Member.drop_table()
# Location.drop_table()
# Exercise.drop_table()
# Program.drop_table()

Boxing = Program(L1, t1, e1, "Basic")
print(Boxing)
print(Boxing.location.city)
print(Boxing.trainer.first_name)
print(Boxing.exercise.name)
print(Boxing.membership_required)
L1.save()
# Boxing.save()

ipdb.set_trace()
