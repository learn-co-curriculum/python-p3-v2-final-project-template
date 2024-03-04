#!/usr/bin/env python3
# lib/debug.py

import ipdb

from models.many_to_many import Locale, Member, Arcade
from models.__init__ import CONN, CURSOR



l1 = Locale("Down Town")
l2 = Locale("Harlem")
l3 = Locale("Murray Hill")
m1 = Member("Isaac")
m2 = Member("Ashe")
a1 = Arcade("Ashe", l1)
a2 = Arcade("ryan", l2)


ipdb.set_trace()
