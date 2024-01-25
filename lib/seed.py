#1/user/bin/env python3 

from models.__init__ import CONN, CURSOR 
from models.exercise import Exercise
from models.location import Location
from models.member import Member
from models.program import Program
from models.trainer import Trainer
# from models.schedule import Schedule

def seed_database():
    # Create tables
    Exercise.create_table()
    Location.create_table()
    Member.create_table()
    Program.create_table()
    Trainer.create_table()

    # Create and save exercises
    exercise1 = Exercise("Spin")
    exercise1.save()
    exercise2 = Exercise("Boxing")
    exercise2.save()
    exercise3 = Exercise("Zumba")
    exercise3.save()

    # Create and save locations
    location1 = Location("Chicago")
    location1.save()
    location2 = Location("St. Louis")
    location2.save()
    location3 = Location("Memphis")
    location3.save()

    # Create and save members
    member1 = Member.create_member_row("Jeffrey", "Davis", "Basic")
    member2 = Member.create_member_row("Katie", "Nowicki", "Premium")
    member3 = Member.create_member_row("Hadil", "Hijazi", "Premium")

    # Create and save trainers
    trainer1 = Trainer("Carol", "Adams")
    trainer1.save()
    trainer2 = Trainer("Joe", "Wilson")
    trainer2.save()
    trainer3 = Trainer("Brenda", "Scott")
    trainer3.save()

    # Create and save programs
    program1 = Program(location1, trainer1, exercise1, "Basic")
    program1.save()
    program2 = Program(location2, trainer2, exercise2, "Premium")
    program2.save()
    program3 = Program(location3, trainer3, exercise3, "Premium")
    program3.save()
    program4 = Program(location2, trainer2, exercise1, "Basic")
    program4.save()

if __name__ == "__main__":
    seed_database()
