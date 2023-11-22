#!/usr/bin/env python3
# lib/debug.py

import ipdb

from models.__init__ import CONN, CURSOR
from models.genre import Genre

genre1 = Genre()

ipdb.set_trace()
