# lib/helpers.py
from models.team import Team

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def list_teams():
    teams = Team.get_all()
    if len(teams) < 1:
        print("\n No teams in database.")
    print("ID", "\t", '{0: <25}'.format("NAME"), "DIVISION")
    for team in teams:
        print(team[0], "\t", '{0: <25}'.format(team[1]), team[2])