# lib/helpers.py
from models.exercise import Exercise
from models.location import Location
from models.member import Member
from models.program import Program
from models.trainer import Trainer
# from models.schedule import Schedule

def exit_program():
    print("Goodbye!")
    exit()

def add_member():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    new_member = Member.create_member_row(None, first_name, last_name)
    print(f'Member {new_member.first_name} {new_member.last_name} has been added with the {new_member.membership_type} membership.')
    return new_member

def change_membership():
    first_name = input("Enter members first name: ")
    last_name = input("Enter members last name: ")
    member = Member.find_by_name(first_name, last_name)
    if member is None:
        print("Member not found")
        return 
    new_membership_type = input("Enter new membership type (Basic/Premium): ")
    if new_membership_type not in ["Basic", "Premium"]:
        print("Invalid membership type")
        return 
    elif member.membership_type == new_membership_type:
        print(f'{member.first_name} already has a {new_membership_type} membership.')
        return 
    member.membership_type = new_membership_type
    member.save()
    print(f"{member.first_name} {member.last_name}'s membership has been changed to {new_membership_type}.")

def view_members():
    members = Member.get_all_members()
    for member in members:
        print(f"{member.first_name} {member.last_name} Membership Type: {member.membership_type}")

def view_classes():
    programs = Program.get_all_programs()
    for program in programs:
        program_id, trainer_name, exercise_name, location_name, membership_required = program
        print(f"Class Info: {program_id}, Trainer: {trainer_name}, Exercise: {exercise_name}, Location: {location_name}, Membership Required: {membership_required}")

def add_class():
    trainer_name = input("Enter trainers name: ")
    exercise_name = input("Enter name of class: ")
    location_name = input("Enter location: ")
    membership_required = input("Choose Basic or Premium")

    trainer = Trainer.find_by_name(trainer_name)
    exercise = Exercise.find_by_name(exercise_name)
    location = Location.find_by_name(location_name)

    if not trainer or not exercise or not location:
        print("Invalid")
        return
    if membership_required not in ["Basic", "Premium"]:
        print("Invalid membership type.")
        return

    new_class = Program(location, trainer, exercise, membership_required)
    new_class.save()

    print(f"Class added: {exercise_name} at {location_name} with Trainer {trainer_name}, Membership Required: {membership_required}")
    return new_class 

def delete_member():
    first_name = input("Enter members first name: ")
    last_name = input("Enter members last_name: ")
    if member := Member.find_by_name(first_name,last_name):
        member.delete()
        print(f"{first_name}{last_name} has been deleted from Flatiron Gym")
    else:
        print("Member not found.")
    
def delete_class():
    program_id = input("Enter program ID to delete: ")
    program = Program.find_by_id(program_id)
    if not program:
        print("Program not found.")
        return 
    Program.delete_by_id(program_id)
    print(f"Program with ID {program_id} has been deleted.")

def delete_trainer():
    first_name = input("Enter trainers first name: ")
    last_name = input("Enter trainers last name: ")
    if trainer := Trainer.find_by_name(first_name, last_name):
        trainer.delete()
        print(f"Trainer {first_name} has been deleted.")
    else:
        print("Trainer not found.")
