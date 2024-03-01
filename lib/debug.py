#!/usr/bin/env python3
# lib/debug.py

import ipdb

from models.many_to_many import Local, Member
from models.__init__ import CONN, CURSOR



l1 = Local("Down Town")
m1 = Member("Ashe", "asheman", 3)


ipdb.set_trace()
