#!/usr/bin/env python3
# lib/debug.py


import ipdb
from classes.Visit import Visit

from classes.Restaurant import Restaurant
from classes.User import User






Restaurant.drop_table()
Restaurant.create_table()

test = Visit(2, "sample description", "sample date", "sample user", "sample restaurant")
test_2 = Visit(2, "sample description", "sample date", "sample user", "sample restaurant")
test_3 = Visit(2, "sample description", "sample date", "sample user", "sample restaurant")
Visit.create(2, "sample description", "sample date", "sample user", "sample restaurant")

test.save()
test_2.save()
test_3.save()
test_3.delete()

ipdb.set_trace()



# def view_all_restaurants():
#     """View all restaurants."""

#     all = Restaurant.get_all()
#     page = [0,20]
#     restaurants = all[page[0]: page[1]]

#     def parse_by_page():
#         pass

#     def next_page():
#         p[0] += 20
#         p[1] += 20
#         restaurants = all[page[0]: page[1]]

#     def prev_page():
#         click.echo('Previous Page')


#     #limit search by 20

#     #print the name and cuisine 
#     for restaurant in restaurants:
#         click.echo(f"{restaurant.id}. {restaurant.name} || {restaurant.cuisine}")