#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from models.team import Team
from models.players import Players

t1 = Team("Wizards", "NE")

p1 = Players("John Wall", t1)

ipdb.set_trace()
