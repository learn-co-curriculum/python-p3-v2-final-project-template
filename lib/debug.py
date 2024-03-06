#!/usr/bin/env python3
# lib/debug.py

import ipdb
from models.arcade import Arcade 
from models.locale import Locale
from models.member import Member
# from models.many_to_many import Locale, Member, Arcade






m1= Member("Isaac", "LVzaack", "l1", "a1", "1")
m2= Member("Parker", "PaawwKa" "l2", "a1", "2")
m3= Member("Desaih", "DDtheDOLL" "l3", "a1", "3") 

l1= Locale("Harlem")
l2= Locale("Brooklyn")
l3= Locale("Down Town")

# a1 = Arcade("Cool People Only Arcade", "1")

ipdb.set_trace()