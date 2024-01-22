# lib/helpers.py
from models.player import Player
from models.level import Level

def create_new_player():
    name = input("What's your name? ")
    player = Player.create(name)
    print(f"Welcome, {name}!")

def list_all_players():
    for player in Player.get_all():
        print(player)

def update_player():
    _id = input("Enter player id: ")

    if player := Player.find_by_id(_id):
        try:
            name = input("Enter player name: ")
            player.name = name
            player.update()
            print(f'Success: {player} updated')
        except Exception as exc:
            print("Error updating employee: ", exc)
    else:
        print(f'Employee {_id} not found')

def delete_player():
    _id = input("Enter player id: ")

    if player := Player.find_by_id(_id):
        try:
            player.delete()
            print(f'Success: {player} deleted')
        except Exception as exc:
            print("Error deleting employee: ", exc)
    else:
        print(f'Employee {_id} not found')

def list_all_levels():
    for level in Level.get_all():
        print(level)

def exit_program():
    print("Goodbye!")
    exit()
