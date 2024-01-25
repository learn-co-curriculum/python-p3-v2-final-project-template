# lib/helpers.py
from models.location import Location
from models.member import Member
from models.program import Program
from models.trainer import Trainer
from models.schedule import Schedule

def exit_program():
    print("Goodbye!")
    exit()

def add_member():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    membership_type = input("Do you want Basic or Premium membership?: ")
    new_member = Member.create(first_name, last_name, membership_type)
    print(f'Member {new_member.first_name} {new_member.last_name} has been added with the {new_member.membership_type} membership.')
    return new_member

def change_membership():
    first_name = input("Enter members first name: ")
    last_name = input("Enter members last name: ")
    member = Member.find_by_name(first_name, last_name)
    if member is None:
        print("Member not found")
        return 
    new_membership_type = input(f"Current Membership is {member.membership_type}. Enter new membership type (Basic/Premium): ")
    if new_membership_type not in ["Basic", "Premium"]:
        print("Invalid membership type")
        return 
    elif member.membership_type == new_membership_type:
        print(f'{member.first_name} already has a {new_membership_type} membership.')
        return 
    member.membership_type = new_membership_type
    member.update()
    print(f"{member.first_name} {member.last_name}'s membership has been changed to {new_membership_type}.")

def view_members():
    members = Member.get_all()
    for member in members:
        print(member)
        # print(f"{member.first_name} {member.last_name} Membership Type: {member.membership_type}")

def view_all_programs():
    programs = Program.get_all()
    for program in programs:
        location = Location.find_by_id(program.location_id)
        trainer = Trainer.find_by_id(program.trainer_id)
        print(f"Program Info: Program ID: {program.id}, Exercise Name: {program.exercise_name}, Trainer: {trainer.first_name} {trainer.last_name}, Location: {location.city}, Membership Required: {program.membership_required}")

def add_program():
    exercise_name = input("Enter name of class/exercise: ")
    trainer_first_name = input("Enter trainer's first name: ")
    trainer_last_name = input("Enter trainer's last name: ")
    location_name = input("Enter location: ")
    membership_required = input("Which membership level is required: Basic or Premium? ")

    trainer = Trainer.find_by_name(trainer_first_name, trainer_last_name)
    location = Location.find_by_name(location_name)

    if not trainer:
        print("No trainer registered by that name.")
    elif not location:
        print("This location does not exist.")
        return
    if membership_required not in ["Basic", "Premium"]:
        print("Invalid membership type.")
        return

    new_program = Program.create(location.id, trainer.id, exercise_name, membership_required)
    # new_program = Program(exercise_name, location.id, trainer.id, membership_required)
    # new_program.save()

    print(f"Program added: {exercise_name} at {location_name} with Trainer {trainer_first_name} {trainer_last_name}, Membership Required: {membership_required}")
    return new_program

def delete_member():
    first_name = input("Enter members first name: ")
    last_name = input("Enter members last_name: ")
    member = Member.find_by_name(first_name, last_name)

    if member:
        member.delete()
        print(f"{first_name} {last_name} has been deleted from Flatiron Gym")
    else:
        print("Member not found.")
    
def delete_program():
    program_id = input("Enter program ID to delete: ")
    program = Program.find_by_id(program_id)
    if not program:
        print("Program not found.")
        return 
    program.delete()
    print(f"{program} has been deleted.")
    pass # Having issues with program.id

def delete_trainer():
    first_name = input("Enter trainers first name: ")
    last_name = input("Enter trainers last name: ")
    if trainer := Trainer.find_by_name(first_name, last_name):
        trainer.delete()
        print(f"Trainer {first_name} has been deleted.")
    else:
        print("Trainer not found.")
