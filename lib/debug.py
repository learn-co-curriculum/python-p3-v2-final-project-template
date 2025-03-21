#!/usr/bin/env python3
# lib/debug.py
#import ipdb
from models.Customer import Customer
from models.Drinks import Drinks
from models.Drink_Orders import DrinkOrder

from models.__init__ import CONN, CURSOR


Jay = Customer(name="Jay", age=23)
Victoria = Customer(name="Victoria", age= 25)
Kerissa = Customer(name="Kerissa", age=33)
Madison = Customer(name="Madison", age=20)
Johnathan = Customer(name="Johnathan", age=18)


#ipdb.set_trace()
