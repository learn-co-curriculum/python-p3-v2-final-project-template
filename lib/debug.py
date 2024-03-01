#!/usr/bin/env python3
# lib/debug.py

import ipdb

from models.many_to_many import Local, Player
from models.__init__ import CONN, CURSOR



l1 = Local("Down Town")
n1 = Player("Ashe", "asheman", 3)


ipdb.set_trace()
