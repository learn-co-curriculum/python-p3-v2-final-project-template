#!/usr/bin/env python3
# lib/debug.py

import ipdb
from models.arcade import Arcade 
from models.locale import Locale
from models.member import Member
# from models.many_to_many import Locale, Member, Arcade
from models.__init__ import CONN, CURSOR



l1 = Locale("Down Town")
l2 = Locale("Harlem")
l3 = Locale("Murray Hill")
m1 = Member("Isaac", "gamertag")
m2 = Member("Asheee", "whodone")
a1 = Arcade(m1, l1)
a2 = Arcade(m2, l2)


ipdb.set_trace()