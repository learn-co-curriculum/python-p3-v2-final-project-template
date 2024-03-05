#!/usr/bin/env python3
# lib/debug.py

import ipdb

from models.__init__ import CONN, CURSOR
from lib.models.arcade import Arcade
from lib.models.member import Member
from lib.models.locale import Locale





l1 = Locale("Down Town")
l2 = ("Harlem")
l3 = ("Murray Hill")
a1 = Arcade("Ashe", "Down Town")
m1 = Member("isaac")


ipdb.set_trace()
