#!/usr/bin/env python3
# lib/debug.py

import ipdb
from models.arcade import Arcade 
from models.locale import Locale
from models.member import Member
# from models.many_to_many import Locale, Member, Arcade
from models.__init__ import CONN, CURSOR



l1 = Locale(1)
l2 = Locale(2)
l3 = Locale(3)
a1 = Arcade("Isaac","doofus", 2)
a2 = Arcade("Asheee", "dinding", 3)
a3 = Arcade("chonkyboi", "yarp", 1)


ipdb.set_trace()