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
    new_member = Member.create_member_row(first_name, last_name, membership_type)
    print(f'Member {new_member.id} {new_member.first_name} {new_member.last_name} has been added with the {new_member.membership_type} membership.')

    return new_member



def change_membership():
    member_id = input("Enter the member's ID: ")
    first_name = input("Enter the member's first name: ")
    last_name = input("Enter the member's last name: ")

    try:
        member_id = int(member_id)
    except ValueError:
        print("Invalid ID format. Please enter a numerical ID.")
        return

    member = Member.find_by_id(member_id)
    if not member:
        print("Member not found")
        return

    if member.first_name == first_name and member.last_name == last_name:
        new_membership_type = input("Enter new membership type (Basic/Premium): ")
        if new_membership_type not in ["Basic", "Premium"]:
            print("Invalid membership type")
            return
        elif member.membership_type == new_membership_type:
            print(f"{member.first_name} already has a {new_membership_type} membership.")
            return
        member.membership_type = new_membership_type
        member.save()
        print(f"{member.first_name} {member.last_name}'s membership has been changed to {new_membership_type}.")
    else:
        print("Member details do not match.")


def view_members():
    members = Member.get_all()
    for member in members:

        print(f"ID: {member.id}, First Name: {member.first_name}, Last Name: {member.last_name}, Membership Type: {member.membership_type}")


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
    method = input("Delete by ID(1) or Name(2)? Enter 1 or 2: ")

    if method == "1":
        member_id = input("Enter the member ID: ")
        try:
            member_id = int(member_id)
            member = Member.find_by_id(member_id)
            if member:
                member.delete()
                print(f"Member with ID {member_id} has been deleted.")
            else:
                print("Member not found.")
        except ValueError:
            print("Invalid ID format. Please enter a numerical ID.")

    elif method == "2":
        first_name = input("Enter the member's first name: ")
        last_name = input("Enter the member's last name: ")
        member = Member.find_by_name(first_name, last_name)
        if member:
            member.delete()
            print(f"Member {first_name} {last_name} has been deleted.")
        else:
            print("Member not found or details do not match.")



def delete_program():
    program_id = input("Enter program ID to delete: ")
    program = Program.find_by_id(program_id)
    if not program:
        print("Program not found.")
        return 
    program.delete()
    print(f"{program} has been deleted.")

def add_trainer():
    first_name = input("Enter trainers first name: ")
    last_name = input("Enter trainers last name: ")
    new_trainer = Trainer.create_trainer_row(first_name, last_name)
    print(f'Trainer {new_trainer.id} {new_trainer.first_name} {new_trainer.last_name} has been added.')

    return new_trainer

def delete_trainer():
    first_name = input("Enter trainers first name: ")
    last_name = input("Enter trainers last name: ")
    if trainer := Trainer.find_by_name(first_name, last_name):
        trainer.delete()
        print(f"Trainer {first_name} has been deleted.")
    else:
        print("Trainer not found.")
