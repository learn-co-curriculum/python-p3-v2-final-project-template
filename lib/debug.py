#!/usr/bin/env python3
# lib/debug.py

import ipdb
from models.arcade import Arcade 
from models.locale import Locale
from models.member import Member
# from models.many_to_many import Locale, Member, Arcade

Arcade.drop_table()
Arcade.create_table()
a1 = Arcade("Dave and Busters")
a1.save()
Locale.create_table()
l1=Locale("Queens")
l1.save()
Member.drop_table()
Member.create_table()
Locale.find_by_location("Queens")




m1= Member("Isaac", "LVzaack", a1.id, l1.id)
m2= Member("Parker", "PaawwKa", a1.id, l1.id)
m3= Member("Desiah", "DDtheDOLL", a1.id, l1.id) 
m1.save()
m2.save()
m3.save()



ipdb.set_trace()