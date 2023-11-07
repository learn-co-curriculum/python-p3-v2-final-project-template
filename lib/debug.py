#!/usr/bin/env python3
# lib/debug.py
from models.Parent import Parent,Child
#from models.Children import Child
from models.__init__ import CONN, CURSOR
import ipdb

Parent.drop_table()
Parent.create_table()
Child.drop_table()
Child.create_table()

Zeus=Parent.create('Zeus','this is a bio')
Hera=Parent.create('Hera','Hera bio')
Metis=Parent.create('Metis','Metis bio')

Athena=Child.create('Athena','Athena bio',Zeus)
Ares=Child.create('Ares','Ares bio',Zeus)


ipdb.set_trace()
