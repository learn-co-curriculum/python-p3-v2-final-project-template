#1/user/bin/env python3 

from models.__init__ import CONN, CURSOR 
from models.exercise import Exercise
from models.location import Location
from models.member import Member
from models.program import Program
from models.trainer import Trainer
from models.schedule import Schedule

def seed_database():
    Member.drop_table()
    