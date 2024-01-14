#!/usr/bin/env python3
# lib/debug.py

import ipdb
from models.__init__ import CONN, CURSOR

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
Boxing = Program(L1, t1, e1, "Basic")
print(Boxing)
print(Boxing.location.city)
print(Boxing.trainer.first_name)
print(Boxing.exercise.name)
print(Boxing.membership_required)
# L1.save()
# Boxing.save()

L1 = Location("Chicago")
L2 = Location("Memphis")   
L3 = Location("St. Louis")
L4 = Location("Louisville")
L5 = Location("Seatle")

t1 = Trainer("Bob", "Thornton") 
t2 = Trainer("Tony", "Little")
t3 = Trainer("Tracy", "Anderson")
t4 = Trainer("Jillian", "Michales")
t5 = Trainer("Bob", "Harper")
t6 = Trainer("Kathy", "Smith")

e1 = Exercise("Boxing")  
e2 = Exercise("Spin Class")
e3 = Exercise("Zumba")
e4 = Exercise("Cycling")
e5 = Exercise("Yoga")   

LocationID = 1
LocationName = "Chicago"
TrainerID = 1 
TrainerFirstName = "Bob"
TrainerLastName = "Thornton"  
ExerciseID = 1  
ExerciseName = Boxing   
MemberID = 1
MemberFirstName = "Jeffrey"   
MemberLastName = "Davis"  
MemberMembership = "Basic"

LocationID = 2
LocationName = "Memphis"
TrainerID = 3
TrainerFirstName = "Tracy" 
TrainerLastName = "Anderson" 
ExerciseID = 2  
ExerciseName = "Spin Class"   
MemberID = 3
MemberFirstName = "Hadil"   
MemberLastName = "Hijazi"  
MemberMembership = "Premium"

LocationID = 4
LocationName = "Louisville"
TrainerID = 2 
TrainerFirstName = "Tony" 
TrainerLastName = "Little" 
ExerciseID = 1  
ExerciseName = Boxing   
MemberID = 2
MemberFirstName = "Katie"   
MemberLastName = "Nowicki"  
MemberMembership = "Premium"



ipdb.set_trace()