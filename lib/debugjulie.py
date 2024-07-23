#!/usr/bin/env python3
# lib/debug.py

from models.owner import Owner
from models.cat import Cat
from models.reservation import Reservation
import ipdb

Reservation.drop_table()
Reservation.create_table()
Reservation.get_all()
test_res1 = Reservation.create(9785510848, 1, 2)
test_res1.phone_number = 9785510847
test_res1.update()

ipdb.set_trace()
