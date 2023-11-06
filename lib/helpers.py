# lib/helpers.py
from models.team import Team

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def list_teams():
    teams = Team.get_all()
    for team in teams:
        print(team)