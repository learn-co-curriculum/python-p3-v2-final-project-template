#!/usr/bin/env python3
# lib/debug.py

from classes.Restaurant import Restaurant
from classes.User import User


Restaurant.drop_table()
Restaurant.create_table()


# test = Restaurant('Restaurant', 'ADDRESS', 'WARD', 'CUISINE', 'PCE', 'WEBSITE', 'MISC', 'AWARD', 'DESCRIPTION')

print(Restaurant.create('Resta55urant', 'ADD55RESS', 'WA555RD', 'CUI5555NE', 'PCE', 'WEBSITE', 'MISC', 'AWARD', 'DESCRIPTION'))