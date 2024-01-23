#!/usr/bin/env python3
# lib/debug.py

from lib.models.model_1 import *

from models.__init__ import CONN, CURSOR
import ipdb

location1 = Location("Chicago")
location2 = Location("St.Louis")
location3 = Location("Memphis")

member1 = Member("Jeffrey", "Davis", "basic")
member2 = Member("Katie", "Nowicki", "premium")
member3 = Member("Hadil", "Hijazi", "premium")



ipdb.set_trace()
