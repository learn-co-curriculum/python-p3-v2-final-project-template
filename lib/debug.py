#!/usr/bin/env python3
# lib/debug.py
from models.player import Player 
from models.world import World

from models.__init__ import CONN, CURSOR
import ipdb
player1 = Player('Matt')
world1 = World('Howling Castle')

ipdb.set_trace()
