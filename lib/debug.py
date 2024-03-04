#!/usr/bin/env python3
# lib/debug.py

import ipdb

from models.many_to_many import Locale, Member, Arcade
from models.__init__ import CONN, CURSOR



l1 = Locale("Down Town")
l2 = ("Harlem")
l3 = ("Murray Hill")
a1 = Arcade("Ashe", "Down Town", 3)
a2 = Arcade("ryan", "Harlem", 2)


ipdb.set_trace()
