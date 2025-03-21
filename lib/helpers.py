# lib/helpers.py
from debug import Jay
from debug import Victoria
from debug import Kerissa
from debug import Madison
from debug import Johnathan

def age_checker():
    if Jay.age > 21:
        print("\nWelcome in!")
    else:
        print("\nSorry gotta go!")
        exit()


def exit_program():
    print("\n See ya later!")
    exit()
