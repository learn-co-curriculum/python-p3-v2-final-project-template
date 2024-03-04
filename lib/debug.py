#!/usr/bin/env python3
# lib/debug.py

import ipdb

from models.many_to_many import Locale, Member, Arcade
from models.__init__ import CONN, CURSOR



l1 = Locale("Down Town")
l2 = Locale("Harlem")
l3 = Locale("Murray Hill")
m1 = Member("Isaac")
m2 = Member("Asheee")
a1 = Arcade(m1, l1)
a2 = Arcade(m2, l2)


ipdb.set_trace()
