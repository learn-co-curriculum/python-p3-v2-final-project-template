#!/usr/bin/env python3
# lib/debug.py

from models.owner import Owner
import ipdb
from models.cat import Cat

Owner.drop_table()
Owner.create_table()
Hollis = Owner.create("Hollis", 7202337895, "274A 5th Ave, San Francisco CA 94118")
Cat.drop_table()
Cat.create_table()
Higgs = Cat.create("Higgs", "shorthair", 1, 2, Hollis.id)

Higgs.owner()
# test
ipdb.set_trace()
