# lib/helpers.py
from models.player import Player

def create_new_player():
    name = input("What's your name? ")
    favorite_color = input("What's your favorite color?")
    player = Player.create(name, favorite_color)
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
            favorite_color = input("Enter player's favorite color: ")
            player.favorite_color = favorite_color
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

def exit_program():
    print("Goodbye!")
    exit()
